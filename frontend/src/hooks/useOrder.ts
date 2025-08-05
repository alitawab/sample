import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query"
import { createOrder, getOrder, getPendingOrders, updateOrderStatus } from "../services/order";
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
  const queryClient = useQueryClient();

  return useQuery({
    queryKey:["orders"],
    queryFn: getOrder
  })
}
export const useOrderByStatus = () => {
    const queryClient = useQueryClient();

    return useQuery({
        queryKey:["orders"],
        queryFn: getPendingOrders
    })

}

export const useOrderUpdateStatus = () => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: ({order_id,nextStatus}:{order_id: number, nextStatus: string}) => updateOrderStatus(order_id,nextStatus),
    onSuccess: () => {
      toast.success("Order accepted!");
      queryClient.invalidateQueries({ queryKey: ["orders"] });
    },
    onError: () => toast.error("Failed to accept order"),
  });
};