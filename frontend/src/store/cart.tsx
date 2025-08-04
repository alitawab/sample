import { createContext, useContext, useState, type ReactNode } from "react";

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
    clearCart: () => void;
}

const CartContext = createContext <CartCtx | undefined>(undefined);



export const CartProvider = ({ children }: { children : ReactNode}) => {
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
    }

    return (
        <CartContext.Provider value={{ cartItems, resturantId, cartCount, addToCart, removeFromCart, updateQuantity, clearCart }}>
            { children }
        </CartContext.Provider>
    );
};

export const useCart = () => {
    const ctx = useContext(CartContext);
    if(!ctx) throw new Error("useCart must be used within a Cart Provider");

    return ctx;
}