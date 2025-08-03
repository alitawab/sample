import { Link, Outlet, useNavigate } from 'react-router-dom';
import { useAuth } from '../store/auth';
import { useCart } from '../store/cart';

export default function MainLayout() {
    const {user, logout}= useAuth();
    const { cartCount } = useCart();
    const navigate = useNavigate()


    const handleDashboardRedirect = () => {
        if(user?.role === 'resturant') navigate('/resturant/dashboard')
        else if(user?.role === 'rider') navigate('/rider/dashboard')
        else if(user?.role === 'user') navigate('/')
                        }

    const handleLogout = () => {
        logout();
        navigate('/');
    }
    return (
        <div className='min-h-screen flex flex-col font-sans'>
            <header className="p-4 bg-black text-white shadow-md">
                <div className='max-w-6xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4'>
                    <Link to='/'>
                        <h1 className='text-xl sm:text-2xl font-bold hover:text-yellow-400 transition'>🍔 Food App</h1>
                    </Link>
                    <div className='flex gap-3 items-center'>
                        <Link to='/cart' className= 'btn btn-sm btn-outline relative'>
                            🛒 Cart
                            {cartCount > 0 && (
                                <span className='ml-2 bg-red-500 text-white rounded-full px-2 text-xs'>
                                    {cartCount}
                                </span>
                            )}
                        </Link>
                    {!user ? (
                        <>
                            <Link to='/login' className='btn btn-sm btn-outline hover:bg-white hover:text-black'>
                                Login
                            </Link>
                            <Link to='/register' className='btn btn-sm btn-outline hover:bg-white hover:text-black'>
                                Register
                            </Link>
                        </>
                    ) : (
                    <>
                        <button onClick={handleDashboardRedirect} className='text-sm sm:text-base hover:underline'>
                            Hi, {user.name}, Role: {user.role}
                        </button>
                        <button onClick={handleLogout} className='btn btn-sm btn-ghost hover:bg-red-600 hover:text-white'>
                            Logout
                        </button>
                    </>
                    )}
                    </div>
                </div>
            </header>
            <main className='flex-1 max-w-6xl mx-auto w-full p-4'>
                <Outlet />
            </main>
            <footer className='p-4 bg-gray-200 text-center text-sm text-gray-600'>
                &copy; {new Date().getFullYear()} Food App. All rights reserved.
            </footer>
        </div>
    );
}