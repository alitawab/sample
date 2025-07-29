import { useAuth } from "../store/auth";

export default function Home() {
    const { user } = useAuth();
    return (
        <div className="space-y-4">
        <h2 className="text-2xl font-bold">Welcome, {user?.name} 👋</h2>
        <p className="text-gray-600">
            You're now inside the protected area of the app.
        </p>
        </div>
        );
}