import { Navigate } from "react-router-dom";
import { useAuth } from "../store/auth";
import { type ReactNode } from "react";

export default function PrivateRoute({children,requiredRole}: {children: ReactNode,requiredRole?:string}) {
    const { user , token } = useAuth();

    if (!token){
        return <Navigate to="/login" replace />
    }
    if(requiredRole && user?.role !== requiredRole) {
        return <Navigate to="/unauthorized" replace />;
    }
    return <>{children}</>
}