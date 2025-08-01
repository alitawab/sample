import { Link, Outlet, useNavigate } from 'react-router-dom';
import { useAuth } from '../store/auth';

export default function MainLayout() {
    const {user, logout}= useAuth();
    const navigate = useNavigate()

    const handleLogout = () => {
        logout();
        navigate('/');

    }
    return (
        <div className='min-h-screen flex flex-col'>
            <header className='p-4 bg-black text-white'>
                <Link to='/'>
                    <h1 className='text-lg font-semibold'>🍔 Food App</h1>
                </Link>
                {!user ? (
                    <div className='space-x-2'>
                        <a href='/login' className='btn btn-sm btn-outline'>Login</a>
                        <a href='/register' className='btn btn-sm btn-outline'>Register</a>
                    </div>
                ):(
                <div className='flex items-center space-x-4'>
                    <button 
                        onClick={() => {
                            if(user.role === 'resturant') navigate('/resturant/dashboard')
                            else if(user.role === 'rider') navigate('/rider/dashboard)')
                            else if(user.role === 'user') navigate('/')
                        }} className='text-sm'>
                        Hi, {user.name}, Role: {user.role}
                    </button>
                    <button onClick={handleLogout} className='btn btn-sm btn-ghost'>Logout</button>
                </div>
                )}

            </header>
            <main className='flex-1 p-4'>
                <Outlet />
            </main>
            <footer className='p-4 bg-gray-100 text-center text-sm text-gray-500'>
                &copy; 2025 Food App
            </footer>
            
        </div>
    );
}