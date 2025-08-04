export interface CartItem {
    menuitem_id: number;
    quantity: number;
    unit_price: number;
}

export interface Address {
    id: number;
    text: string;
    latitude: number;
    longitude: number;
}

export interface CreateOrderPayload {
    user_id: number|null;
    address: Address;
    resturant_id: number|null;
    rider_id: null;
    total_price: number;
    status: string;
    created_at: string;
    payment_method: string;
    items: CartItem[];

}