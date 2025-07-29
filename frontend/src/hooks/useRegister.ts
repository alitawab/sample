import { useMutation } from "@tanstack/react-query";
import toast from "react-hot-toast";
import { useNavigate } from "react-router-dom"
import { registerUser } from "../services/auth";


export const useRegister = () => {
    const navigate = useNavigate();

    return useMutation({
        mutationFn: registerUser,
        onSuccess: () => {
            toast.success('Registration successful! Please login.')
            navigate('/login')
        },
        onError: (err: any) => {
        toast.error(err?.response?.data?.message || 'Registration failed')
        },
    })
}