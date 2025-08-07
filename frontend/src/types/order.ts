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

export interface Order {
  order_id: number;
  status: string;
  total_price: number;
  payment_method: string;
  restaurant_id: number;
  rider_id?: number;
  location: {
    lat: number;
    lng: number;
  };
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