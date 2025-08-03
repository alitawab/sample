import { useState } from "react";
import PaymentModal from "../components/PaymentModal";
import toast from "react-hot-toast";
import { useCart } from "../store/cart";
import AddressModal from "../components/AddressModal";
import { useNavigate } from "react-router-dom";


export default function Checkout() {
    const { cartItems, clearCart } = useCart();

    const [ selectedAddress, setSelectedAddress ] = useState<{id:number; text:string;} |null>(null);
    const [paymentMethod, setPaymentMethod] = useState<string | null>(null);
    
    const [isAddressModalOpen, setIsAddressModalOpen] = useState(false);
    const [isPaymentModalOpen, setIsPaymentModalOpen] = useState(false);


    const total = cartItems.reduce((sum,i) => sum + i.price * i.quantity, 0)
    const navigate = useNavigate();

    const handleComplete = () => {
        toast("Order Placed");
        clearCart();
        setSelectedAddress(null);
        setPaymentMethod(null);
        navigate('/');
    }

    const handleConfirmPayment = () => {
        setIsPaymentModalOpen(false);
    }

    function AddressDetails({ address }: { address: string }) {
        const [house, street, area] = address.split(',');
        return (
        <p className="border-b mb-2 p-2">
            <strong>House No:</strong> {house} <br />
            <strong>Street No:</strong> {street} <br />
            <strong>Area:</strong> {area}
        </p>
        );
    }

    return(
        <div className="max-w-3xl mx-auto p-4">
            <h1 className="text-2xl font-semibold mb-4">Checkout</h1>
            
            <div className="space-y-6 mb-20">
                {cartItems.map(item => (
                    <div key={item.id} className="flex item-center justify-between border-b pb-2">
                        <div>
                            <h4 className="text-lg font-semibold">{item.name}</h4>
                            <p className="text-sm text-gray-600">{item.price.toFixed(2)}</p>
                        </div>
                        <div className="flex items-center gap-2">
                            <h5 className="text-md font-semibold"> X {item.quantity}</h5>
                        </div>
                    </div>
                ))}
                <div className="text-right font-semibold text-lg pt-4">
                    Total: Rs - {total.toFixed(2)} 
                </div>
                <div>
                {selectedAddress && (
                    <>
                        <p className="font-semibold mb-1">Order will be delieverd at :</p>
                        <AddressDetails address = {selectedAddress.text}/>
                    </>
                )}
                {paymentMethod && (
                    <p>Selected Payment : {paymentMethod?.toUpperCase()}</p>
                )}
                </div>
                </div>
                
                <div className="space-y-4">
                    {!selectedAddress ? (
                        <button onClick={() => setIsAddressModalOpen(true)} className="btn btn-outline w-full">
                            Select Address For Delivery
                        </button>
                    ):(
                        <div className="space-y-2">
                            <div className="text-sm text-gray-400">
                                {!paymentMethod && (
                                    <button onClick={() => setIsPaymentModalOpen(true)}
                                    className="btn btn-outline w-full">
                                        Select Payment Method
                                    </button>
                                )}
                            </div>
                        </div>
                    )}
                    {selectedAddress && paymentMethod && (
                        <button onClick={handleComplete} className="btn btn-primary w-full">Place Order</button>
                    )}
                </div>
                <PaymentModal 
                isOpen={isPaymentModalOpen}
                onClose = {() => {setIsPaymentModalOpen(false); setPaymentMethod(null)}}
                paymentMethod = {paymentMethod}
                setPaymentMethod = {setPaymentMethod}
                onConfirm = {handleConfirmPayment}
                />
                <AddressModal 
                isOpen={isAddressModalOpen}
                onClose={()=>setIsAddressModalOpen(false)}
                onSave={(newAddress) => {
                    setSelectedAddress(newAddress);
                    setIsAddressModalOpen(false)
                }}
                />
            </div>
        )
    }