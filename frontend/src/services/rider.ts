import { api } from "./axios"


export const getRider = async () => {
    const res = await api.get('/resturant');
    return res.data;
}

export const getRiderById = async (rider_id:number) => {
    const res = await api.get(`/rider/${rider_id}`);
    return res.data;
}

export const getRiderByUserId = async (id:any) => {
    const res = await api.get(`/rider/user/${id}`);
    return res.data;
}

export const updateRider = async(id:any, data:FormData) => {

}

export const deleteRider = async(id:any) =>{
    
}