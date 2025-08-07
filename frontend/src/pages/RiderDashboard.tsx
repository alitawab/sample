import { Navigate } from "react-router-dom";
import { useAuth } from "../store/auth";
import { useState } from "react";
import RiderProfile from "../components/RiderProfile";
import RiderOrderManager from "../components/RiderOrderManager";


export default function RiderDashboard() {
    const {user} = useAuth()
    const [activeTab, setActiveTab]= useState("profile")

    if(!user || user.role!== "rider") {
        return <Navigate to="/login" replace />;
    }

    return (
        <div className="p-4 max-w-4xl mx-auto">
            <h1 className="text-2xl font-bold mb-4">Rider Dashboard</h1>
            <div className="flex gap-4 mb-6">
                <button
                className={`btn ${activeTab === "profile" ? "btn-primary":"btn-outline"}`}
                onClick={() => setActiveTab("profile")}
                >
                    Profile
                </button>
                <button
                className={`btn ${activeTab === "activityLog" ? "btn-primary": "btn-outline"}`}
                onClick={() => setActiveTab("activityLog")}
                >
                    Activity Log
                </button>
                <button
                className={`btn ${activeTab === "orders" ? "btn-primary": "btn-outline"}`}
                onClick={() => setActiveTab("orders")}
                >
                    Check New Orders
                </button>
            </div>
            {activeTab ==="profile" && <RiderProfile rider_id = {user.role_id}/>}
            {/* {activeTab === "activityLog" && <ActivityLog rider_id = {user.role_id}/>} */}
            {activeTab === "orders" && <RiderOrderManager rider_id = {user.role_id}/>}
        </div>
    )
}