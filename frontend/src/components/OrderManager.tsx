import toast from "react-hot-toast";
import { useOrder, useOrderByStatus, useOrderUpdateStatus } from "../hooks/useOrder"


const nextStatusMap: Record<string, string | null> = {
  Pending: "Accepted",
  Accepted: null, // Rider will handle next
  "Assigned to Rider": "Ready for Pickup",
  "Ready for Pickup": "Out for Delivery",
  "Out for Delivery": "Delivered",
  Delivered: null,
};

export default function OrderManager({resturant_id}:{resturant_id:number}) {
    const {data:orders=[], isLoading} = useOrder();

    const { mutate:updateStatus } = useOrderUpdateStatus();

    const updateOrderStatusHandler = (order_id:number, status: string) => {
        const nextStatus = nextStatusMap[status];
        if(!nextStatus){
            toast.error("No further action avilable");
            return;
        }
        updateStatus({order_id, nextStatus})
    }

    return (
        <div>
            <h2 className="text-xl font-semibold mb-4">Pending Orders</h2>
            {orders.length === 0 ? (
                <p>No Pending Orders</p>
            ):(
                <ul className="space-y-4">
                    {orders.map((order:any) => (
                        <li key={order.order_id} className="p-4 border rounded shadow-sm">
                            <p><strong>Order ID:</strong>{order.order_id}</p>
                            <p><strong>Total:</strong>{order.total_price}</p>
                            <p><strong>Payment:</strong>{order.payment_method.toUpperCase()}</p>
                            <p><strong>Order Status:</strong>{order.status}</p>
                            {nextStatusMap[order.status] && (
                                <button onClick={() => updateOrderStatusHandler(order.order_id, order.status)} className="btn btn-sm btn-success mt-2">
                                    Mark as : {nextStatusMap[order.status]}
                                </button>

                            )}
                        </li>
                    ))}
                </ul>
            )}

        </div>
    )
}