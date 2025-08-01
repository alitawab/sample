import { api } from "./axios";

export const getMenuItems = async () => {
    const res = await api.get('/menuitem')
    return res.data;
}


export const getMenuItemById = async (id:any) => {
    const res = await api.get(`/menuitem/${id}`)
    return res.data;
}


export const addMenuItem = async (formData:FormData) => {
    const res = await api.post('/menuitem', formData, {
        headers:{"Content-Type": "multipart/form-data"},
    });
    return res.data;
}

export const updateMenuItem = async (id:number , formData:FormData) => {
    const res = await api.put(`/menuitem/${id}`, formData, {
        headers:{"Content-Type": "multipart/form-data"},
    });
    return res.data;
}

export const getMenuItemByResturantId = async (id:any) => {
    const res = await api.get(`/menuitem/resturant/${id}`)
    return res.data;
}

export const deleteMenuItem = async (id:any) => {
    const res = await api.delete(`/menuitem/${id}`)
    return res.data;
}
