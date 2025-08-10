import { createContext, useContext, useEffect, useState, type ReactNode } from "react";
import { getCartFromBackend, syncCartToBackend } from "../services/cart";

interface CartItem {
    menuitem_id:number;
    name:string;
    price:number;
    quantity:number;
}
interface CartCtx {
    cartItems: CartItem[];
    resturantId: number|null;
    cartCount: number;
    addToCart: (item:CartItem, resturant_id: number) => void;
    removeFromCart: (id:number) => void;
    updateQuantity: (id:number, qty:number) => void;
    saveCartToBackend: (user_id?:number) => void;
    clearCart: () => void;
}

const CartContext = createContext <CartCtx | undefined>(undefined);



export const CartProvider = ({ children }: { children : ReactNode}) => {

    useEffect(()=>{
        const fetchCart = async () => {
            const guest_token = localStorage.getItem("guest_token")
            if(!guest_token) return;

            try {
                const data = await getCartFromBackend(guest_token);
                if(data && data.cart_details?.length) {
                    const item = data.cart_details.map((details:any) => ({
                        menuitem_id: details.menuitem_id,
                        name: details.menuitem.name,
                        price: details.menuitem.price,
                        quantity: Number(details.quantity)
                    }));
                    setCartItems(item);
                    localStorage.setItem("cartItem", JSON.stringify(item))
                    localStorage.setItem("resturantId",data.cart_details[0].menuitem.resturant_id)
                    setResturantId(data.cartdetails[0].menuitem.resturant_id)
                }
            } catch (error) {
                console.error("Failed to get cart",error)
            }
            if(cartItems.length === 0) {
                fetchCart();
            }
        }
    },[])

    const [resturantId, setResturantId] = useState<number|null>(() => {
        const stored = localStorage.getItem("resturantId");
        return stored ? Number(stored) : null
    })
    const [cartItems, setCartItems] = useState<CartItem[]>(() => {
        const stored = localStorage.getItem("cartitem");
        return stored ? JSON.parse(stored) : [];
    });

    const cartCount = cartItems.reduce((sum, item) => sum + item.quantity,0);
    
    const addToCart = (item: CartItem, itemResturantId: number) => {
        if(cartItems.length ==0){
            setResturantId(itemResturantId);
            localStorage.setItem("resturantId", itemResturantId.toString())
            setCartItems([{...item, quantity:1}]);
            return;
        }

        if(itemResturantId !== resturantId) {
            alert("You can only add items from one resturant at a time. Please clear your cart first.");
            return;
        }

        setCartItems(prev => {
            const existing = prev.find(i => i.menuitem_id === item.menuitem_id);
            let newCart;
            if(existing) {
                newCart = prev.map(i => 
                    i.menuitem_id === item.menuitem_id ? {...i, quantity : i.quantity + 1} : i
                );
            } else {
                newCart = [...prev, {...item, quantity:1}];
            }
            localStorage.setItem("cartitem",JSON.stringify(newCart));
            return newCart
        });
    };

    const removeFromCart = (id: number) => {
        setCartItems(prev => {
            const newCart = prev.filter(item => item.menuitem_id !== id)
            localStorage.setItem("cartitem",JSON.stringify(newCart))
            return newCart
        });
    };

    const updateQuantity = (id: number, qty: number) => {
        setCartItems(prev => {
            const newCart = prev.map(item =>
                item.menuitem_id === id ? {...item, quantity: qty}: item
            );
            localStorage.setItem("cartitem",JSON.stringify(newCart));
            return newCart;
        });
    };


    const clearCart = () => {
        setCartItems([]);
        setResturantId(null);
        localStorage.removeItem("cartitem");
        localStorage.removeItem("resturantId");
        localStorage.removeItem("guest_token")
    }

    const saveCartToBackend = async (user_id?:number) => {
        const guest_token = localStorage.getItem("guest_token") || crypto.randomUUID();
        localStorage.setItem("guest_token",guest_token);

        try {
            const payload = {
            user_id:user_id||null,
            guest_token,
            cart_details: cartItems.map(item => ({
                menuitem_id: item.menuitem_id,
                quantity: item.quantity,
            })),
            status:"active",
        };
        await syncCartToBackend(payload)
        console.log("cart synced")
        } catch (error){
            console.error("failed to sync",error)
        }
    };

    return (
        <CartContext.Provider value={{ cartItems, resturantId, cartCount, addToCart, removeFromCart, updateQuantity, saveCartToBackend, clearCart }}>
            { children }
        </CartContext.Provider>
    );
};

export const useCart = () => {
    const ctx = useContext(CartContext);
    if(!ctx) throw new Error("useCart must be used within a Cart Provider");

    return ctx;
}