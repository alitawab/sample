import { createContext, useContext, useEffect, useState, type ReactNode } from "react";
import type { LoginResponse, User } from "../types/auth";

interface AuthCtx {
    token: string | null
    user: User | null
    login: (data: LoginResponse) => void
    logout: () => void
}

const AuthContext = createContext< AuthCtx | null>(null)

export function AuthProvider ({ children } : {children:ReactNode}) {
    const [token, setToken] = useState<string | null>(null);
    const [user, setUser] = useState<User | null>(null);

    useEffect(() => {
        const t = localStorage.getItem('token');
        const u = localStorage.getItem('user');

        if(t) setToken(t);
        if(u) setUser(JSON.parse(u));
    }, []);

    const login = (data:LoginResponse) => {
        setToken(data.token)
        setUser(data.user)
        localStorage.setItem('token', data.token)
        localStorage.setItem('user', JSON.stringify(data.user))

    }

    const logout = () => {
        setToken(null);
        setUser(null);
        localStorage.removeItem('token');
        localStorage.removeItem('user');
    }

    return (
        <AuthContext.Provider value={{ token, user, login, logout }}>
            {children}
        </AuthContext.Provider>
    )
}

export const useAuth = () => {
    const ctx = useContext(AuthContext);
    if (!ctx) throw new Error("useAuth must be used within an AuthProvider");
    return ctx;
}