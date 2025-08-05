import type { CreateOrderPayload } from "../types/order";
import { api } from "./axios"


export const getOrder = async () => {
    const res = await api.get('/order');
    console.log(res.data)
    return res.data;
}

export const getPendingOrders = async () => {
    const res = await api.get('/order/status');
    return res.data;
}

export const createOrder = async (order: CreateOrderPayload) => {
    const res = await api.post('/order', order);
    return res.data;
}

export const updateOrderStatus = async (orderId: number, status: string) => {
    const res = await api.put(`/order/${orderId}`, { status })
    return res.data
}