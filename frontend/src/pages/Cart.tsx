import { useCart } from "../store/cart"
import { useNavigate } from "react-router-dom";


export default function Cart() {
    const navigate = useNavigate();
    const {cartItems, removeFromCart, updateQuantity, clearCart, saveCartToBackend} = useCart();
    const total = cartItems.reduce((sum: any ,item: any) => sum + item.price * item.quantity, 0);


    const handleProceedToCheckout = () => {
        saveCartToBackend();
        navigate('/checkout');

    }

    return (
        <div className="max-w-3xl mx-auto p-4">
            <h2 className="text-2xl font-bold mb-4">Your Cart</h2>
            {cartItems.length === 0 ?  (
                <p className="text-gray-600">Your cart is empty.</p>
            ):(
                <div className="space-y-6">
                    {cartItems.map(item => (
                        <div key={item.menuitem_id} className="flex item-center justify-between border-b pb-2">
                            <div>
                                <h4 className="text-lg font-semibold">{item.name}</h4>
                                <p className="text-sm text-gray-600">Rs - {item.price.toFixed(2)}</p>
                            </div>
                            <div className="flex items-center gap-2">
                                <input 
                                type="number"
                                value={item.quantity}
                                min={1}
                                onChange={(e) => {updateQuantity(item.menuitem_id,parseInt(e.target.value) || 1)}}
                                className="w-16 border rounded px-2 py-1 text-center" 
                                />
                                <button
                                onClick={() => removeFromCart(item.menuitem_id)}
                                className="text-red-500 hover:text-red-700 text-xl">
                                    ✖
                                </button>
                            </div>
                        </div>
                    ))}
                    <div className="text-right font-semibold text-lg pt-4">
                        Total: Rs - {total.toFixed(2)}
                    </div>
                    <div className="flex justify-end gap-4 mt-4">
                        <button
                        onClick={clearCart}
                        className="px-4 py-2 bg-gray-400 rounded hover:bg-gray-600"
                        >
                            Clear Cart
                        </button>
                        <button onClick={handleProceedToCheckout} className="px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600">
                            Proceed to Checkout
                        </button>
                    </div>
                </div>
            )}
        </div>
    );
}