import toast from "react-hot-toast";
import { useOrderByStatus, useOrderUpdateStatus } from "../hooks/useOrder"
import { reverseGeocode } from "../utils/reverseGeocode";
import { useEffect, useState } from "react";
import { MapContainer, TileLayer } from "react-leaflet";
import OrderRouteMap from "./OrderRouteMap";


const nextStatusMap: Record<string, string | null> = {
  Accepted: "Assigned to Rider",
  "Ready for Pickup": "Out for Delivery",
  "Out for Delivery": "Delivered",
  Pending: null,
  "Assigned to Rider": null,
  Preparing: null,
  Delivered: null,
};

const riderHandledStatuses = ["Accepted","Assigned to Rider", "Ready for Pickup", "Out for Delivery"];

export default function RiderOrderManager({rider_id}:{rider_id:number}) {
    const {data:orders=[], isLoading} = useOrderByStatus(riderHandledStatuses,rider_id);
    const [addresses, setAddresses] = useState<Record<number,string>>({});
    const { mutate:updateStatus } = useOrderUpdateStatus();
    
    useEffect(() => {
        const fetchAddresses = async () => {
            const newAddresses: Record<number, string> = {};
            for (const order of orders) {
                const { latitude, longitude } = order.address || {};
                if (latitude && longitude) {
                    const fullAddress = await reverseGeocode(latitude, longitude);
                    if (fullAddress) {
                        newAddresses[order.order_id] = fullAddress;
                    }
                }
            }
            setAddresses(newAddresses);
        };
        fetchAddresses();
    }, [orders]);




    const updateOrderStatusHandler = (order_id:number, status: string) => {
        const nextStatus = nextStatusMap[status];
        if(!nextStatus){
            toast.error("No further action avilable");
            return;
        }

        if (status === "Accepted") {
            updateStatus({order_id, nextStatus, rider_id})
        } else {
            updateStatus({order_id,nextStatus})
        }
    }
    
    return (
        <div>
            <h2 className="text-xl font-semibold mb-4">Orders</h2>
            {orders.length === 0 ? (
                <p>No Orders</p>
            ):(
                <ul className="space-y-4">
                    {orders.map((order:any) => (
                        <li key={order.order_id} className="p-4 border rounded shadow-sm">
                            <p><strong>Order ID:</strong>{order.order_id}</p>
                            <p><strong>Total:</strong>{order.total_price}</p>
                            <p><strong>Payment:</strong>{order.payment_method.toUpperCase()}</p>
                            <p><strong>Order Status:</strong>{order.status}</p>
                            <p><strong>Address : </strong>{addresses[order.order_id] || "Loading Address..."}</p>
                            {nextStatusMap[order.status] && (
                                <button onClick={() => updateOrderStatusHandler(order.order_id, order.status)} className="btn btn-sm btn-success mt-2">
                                    {order.status === "Accepted" ? "Accept Delivery" : `Mark as : ${nextStatusMap[order.status]}`}
                                </button>

                            )}
                            {order.address?.latitude && order.address?.longitude && order.status === "Out for Delivery" && (
                                <div className="my-4">
                                    <OrderRouteMap destination={{ lat: order.address.latitude, lng: order.address.longitude }} />
                                </div>
                            )}
                        </li>
                    ))}
                </ul>
            )}

        </div>
    )
}