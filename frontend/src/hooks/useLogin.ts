import { useMutation } from "@tanstack/react-query"
import toast from "react-hot-toast"
import { login as loginRequest} from "../services/auth"
import { useAuth } from "../store/auth"
import { useNavigate } from "react-router-dom"


export const useLogin = () => {
    const {login} = useAuth();
    const navigate = useNavigate();
    return useMutation({
        mutationFn: loginRequest,
        onSuccess: (data) => {
            toast.success("Login Successful")
            console.log('Login response:', data)
            login(data)
            navigate('/');
        },
        onError: (error:any) => {
            toast.error(error.response?.data?.message || "Login Failed")
        },
    })
}