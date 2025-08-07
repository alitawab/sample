import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query"
import { createOrder, getOrder, updateOrderStatus, getOrderByStatus, getOrderByResturant } from "../services/order";
import toast from "react-hot-toast";
import { useNavigate } from "react-router-dom";
import type { CreateOrderPayload } from "../types/order";


export const useOrderCreate = () => {
    const navigate = useNavigate();

    const queryClient = useQueryClient();
    return useMutation({
        mutationFn:(payload: CreateOrderPayload) => createOrder(payload),
        onSuccess:() => {
            toast("Order Placed Succesfully");
            navigate('/');
            queryClient.invalidateQueries({queryKey:["orders"]})
        },
        onError: () => {
            toast.error("Failed to place order");
        }
    })
}

export const useOrder = () => {
  return useQuery({
    queryKey:["orders"],
    queryFn: getOrder
  })
}

export const useOrderByResturant = (resturant_id:number) => {
  
  return useQuery({
    queryKey:["orders"],
    queryFn: () => getOrderByResturant(resturant_id)
  })
}


export const useOrderByStatus = (statuses:string | string[], rider_id: number) => {
  const queryKey = Array.isArray(statuses) ? statuses.join(","): statuses;
  return useQuery({
    queryKey:["orders","statuses",queryKey],
    queryFn: () => getOrderByStatus(statuses,rider_id),
  })

}

export const useOrderUpdateStatus = () => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: ({order_id,nextStatus,rider_id}:{order_id: number, nextStatus: string,rider_id?:number}) => 
      updateOrderStatus(order_id,nextStatus,rider_id),
    onSuccess: () => {
      toast.success("Order accepted!");
      queryClient.invalidateQueries({ queryKey: ["orders"] });
    },
    onError: () => toast.error("Failed to accept order"),
  });
};