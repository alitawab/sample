import { useMutation, useQueryClient } from "@tanstack/react-query"
import { createOrder } from "../services/order";
import toast from "react-hot-toast";
import { useNavigate } from "react-router-dom";
import type { CreateOrderPayload } from "../types/order";


export const useOrder = () => {
    const navigate = useNavigate();

    const queryClient = useQueryClient();
    return useMutation({
        mutationFn:(payload: CreateOrderPayload) => createOrder(payload),
        onSuccess:() => {
            toast("Order Placed Successufluuy");
            navigate('/');
            queryClient.invalidateQueries({queryKey:["orders"]})
        },
        onError: () => {
            toast.error("Failed to place order");
        }
    })
}