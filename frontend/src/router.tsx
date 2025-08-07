import { createBrowserRouter } from "react-router-dom";
import MainLayout from "./layouts/MainLayout";
import Home from "./pages/Home";
import Login from "./pages/Login";
import PrivateRoute from "./components/PrivateRoute";
import Register from "./pages/Register";
import ResturantPage from "./pages/ResturantPage";
import MenuItem from "./pages/MenuItem";
import ResturantDashboard from "./pages/ResturantDashboard";
import ErrorPage from "./components/ErrorPage";
import Cart from "./pages/Cart";
import Checkout from "./pages/Checkout";
import RiderDashboard from "./pages/RiderDashboard";


export const router = createBrowserRouter([
    { 
        path: '/',
        element: <MainLayout />,
        errorElement:<ErrorPage />,
        children: [
            { index:true, element:<Home /> },
            { path: '/home', element: <Home /> },
            { path: '/login',element: <Login /> },
            { path: '/register',element: <Register /> },
            { path: '/resturant/:id', element: <ResturantPage /> },
            { path: '/item/:id' ,element: <MenuItem /> },
            { path: '/resturant/dashboard', element:
                (
                    <PrivateRoute requiredRole="resturant">
                        <ResturantDashboard />
                    </PrivateRoute>
                )
            },
            { path:'/rider/dashboard', element:
                (
                    <PrivateRoute>
                        <RiderDashboard />
                    </PrivateRoute>
                )
            },
            { path: '/cart', element: <Cart /> },
            { path: '/checkout', element: <Checkout />}
    ]},
])