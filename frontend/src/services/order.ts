import type { CreateOrderPayload } from "../types/order";
import { api } from "./axios"

export const getOrder = async () => {
    const res = await api.get('/order');
    return res.data;
}

export const getOrderByResturant = async (resturant_id:number) => {
    const res = await api.get(`/order/resturant?resturant_id=${resturant_id}`);
    return res.data;
}


export const getOrderByStatus = async (statuses: string | string[],rider_id:number) => {
    const statusArray = Array.isArray(statuses) ? statuses: [statuses];
    const queryParam = statusArray.map((s) => `status=${encodeURIComponent(s)}`).join("&");
    const res = await api.get(`/order/status?${queryParam}&rider_id=${rider_id}`);
    return res.data;
}

export const createOrder = async (order: CreateOrderPayload) => {
    const res = await api.post('/order', order);
    return res.data;
}

export const updateOrderStatus = async (orderId: number, status: string,rider_id?:number) => {
    const payload: { status: string; rider_id?: number } = { status };
    if (rider_id !== undefined) {
        payload.rider_id = rider_id;
    }
    const res = await api.put(`/order/${orderId}`, { payload })
    return res.data
}