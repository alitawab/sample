import { Navigate } from "react-router-dom";
import { useAuth } from "../store/auth";
import { useState } from "react";
import MenuManager from "../components/MenuManager";
import ResturantProfile from "../components/ResturantProfile";


export default function ResturantDashboard() {
    const {user} = useAuth()
    const [activeTab, setActiveTab]= useState("profile")

    if(!user || user.role!== "resturant") {
        return <Navigate to="/login" replace />;
    }

    return (
        <div className="p-4 max-w-4xl mx-auto">
            <h1 className="text-2xl font-bold mb-4">Resturant Dashboard</h1>
            <div className="flex gap-4 mb-6">
                <button
                className={`btn ${activeTab === "profile" ? "btn-primary":"btn-outline"}`}
                onClick={() => setActiveTab("profile")}
                >
                    Profile
                </button>
                <button
                className={`btn ${activeTab === "menu" ? "btn-primary": "btn-outline"}`}
                onClick={() => setActiveTab("menu")}
                >
                    Menu Item
                </button>
            </div>
            {activeTab ==="profile" && <ResturantProfile resturant_id = {user.resturant_id}/>}
            {activeTab === "menu" && <MenuManager resturant_id = {user.resturant_id}/>}
        </div>
    )
}