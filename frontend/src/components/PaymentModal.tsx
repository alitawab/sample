
interface PaymentModalProps {
    isOpen: boolean;
    onClose: () => void;
    paymentMethod: string | null;
    setPaymentMethod: (method: string) => void;
    onConfirm: () => void;
}

export default function PaymentModal ({isOpen, onClose, paymentMethod, setPaymentMethod, onConfirm}: PaymentModalProps) {

    if (!isOpen) return null;
    return (
        <div className="fixed inset-0 bg-black bg-opacity-40 flex items-center justify-center z-50">
            <div className="bg-gray-400 rounded p-6 max-w-sm w-full">
                <h2 className="text-xl font-semibold mb-4">Select Payment Method</h2>
                <div className="flex flex-col gap-3 mb-6">
                    <label className="flex items-center gap-2 cursor-pointer">
                        <input type="radio" name="payment" value="cod" checked={paymentMethod==="cod"} onChange={() => setPaymentMethod("cod")}/>
                        <span>Cash On Delivery (COD)</span>
                    </label>
                    <label className="flex items-center gap-2 cursor-pointer">
                        <input type="radio" name="payment" value="card" checked={paymentMethod==="card"} onChange={() => setPaymentMethod("card")}/>
                        <span>Card Payment</span>
                    </label>
                     <label className="flex items-center gap-2 cursor-pointer">
                        <input type="radio" name="payment" value="jazzcash" checked={paymentMethod==="jazzcash"} onChange={() => setPaymentMethod("jazzcash")}/>
                        <span>Jazz Cash (Mobile-Wallet)</span>
                    </label>
                    
                </div>
                <div className="flex justify-end gap-3">
                    <button onClick={onClose} className="px-4 py-2 bg-gray-300 rounded hover:bg-gray-500">Cancel</button>
                    <button onClick={onConfirm} disabled={!paymentMethod} className={`px-4 py-2 rounded text-white ${paymentMethod ? 'bg-green-600 hover:bg-green-800':'bg-gray-400 cursor-not-allowed'}`}>Confirm</button>
                </div>
            </div>
        </div>
    )
}