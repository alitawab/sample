import { useMutation } from "@tanstack/react-query"
import toast from "react-hot-toast"
import { login as loginRequest} from "../services/auth"
import { useAuth } from "../store/auth"
import { useNavigate } from "react-router-dom"
import { getResturantByUserId } from "../services/resturant"
import { getRiderByUserId } from "../services/rider"


export const useLogin = () => {
    const {login} = useAuth();
    const navigate = useNavigate();
    return useMutation({
        mutationFn: loginRequest,
        onSuccess: async (data) => {
            const role = data.user.role;
            if(role === "user") navigate('/home');
            else if(role === "resturant") {
                const resturant = await getResturantByUserId(data.user.user_id)
                data.user.role_id = resturant.resturant_id;
                navigate('/resturant/dashboard')
            }
            else if(role === "rider") {
                const rider = await getRiderByUserId(data.user.user_id)
                data.user.role_id = rider.rider_id;
                navigate('/rider/dashboard')
            }
            login(data)
            toast.success("Login Successful")
        },
        onError: (error:any) => {
            toast.error(error.response?.data?.message || "Login Failed")
        },
    })
}