import { api } from "./axios"


export const getResturant = async () => {
    const res = await api.get('/resturant');
    return res.data;
}

export const getResturantById = async (id:any) => {
    const res = await api.get(`/resturant/${id}`);
    return res.data;
}

export const getResturantByUserId = async (id:any) => {
    const res = await api.get(`/resturant/user/${id}`);
    return res.data;
}

export const updateRestaurant = async(id:any, data:FormData) => {

}

export const deleteRestaurant = async(id:any) =>{
    
}