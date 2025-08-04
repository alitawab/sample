import type { CreateOrderPayload } from "../types/order";
import { api } from "./axios"


export const getOrder = async() => {
    const res = await api.get('/order');
    return (res).data;
}
export const createOrder = async (order: CreateOrderPayload) => {
    const res = await api.post('/order', order);
    return res.data;
}