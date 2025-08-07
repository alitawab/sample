export type Rider = {
  rider_id: number;
  user_id: number;
  name: string;
  phone: string;
  vehicle_type: string;
  license_number: string;
  current_location_lat: number;
  current_location_lng: number;
  is_available: boolean;
};