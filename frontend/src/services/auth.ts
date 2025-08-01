import {api} from "./axios";
import type { LoginResponse } from "../types/auth";



export const login = async (payload: {
    email: string,
    password: string
}): Promise<LoginResponse> => {
    const response = await api.post(`/auth/login`, payload)
    return response.data;
    }

export const registerUser = async (data: FormData)  => {
    const res = await api.post('/auth/register', data,{
        headers:{"Content-Type": "multipart/form-data"},
    });
    return res.data;
}
