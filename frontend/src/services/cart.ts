import { api } from "./axios";

export const syncCartToBackend = async (payload:{
    user_id:number|null;
    guest_token:string;
    cart_details:{menuitem_id:number,quantity:number}[];
    status:string;
}) => {
    const res = await api.post('/cart',payload)
    return res.data;
}

export const getCartFromBackend = async (guest_token: string, user_id?: number) => {
    const query = user_id ? `user_id=${user_id}` : `guest_token=${guest_token}`;
    const res = await api.get(`/cart?${query}`)
    return res.data;
}
