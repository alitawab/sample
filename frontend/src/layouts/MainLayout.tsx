import { Outlet } from 'react-router-dom';
import { useAuth } from '../store/auth';

export default function MainLayout() {
    const {user, logout}= useAuth();

    return (
        <div className='min-h-screen flex flex-col'>
            <header className='p-4 bg-black text-white'>
                <h1 className='text-lg font-semibold'>🍔 Food App</h1>
                {user && (
                    <div className='flex items-center gap-4 text-sm'>
                        <span className='text-gray-200'>Hi, {user.name}</span>
                        <button
                        onClick={logout}
                        className='bg-white text-black px-3 py-1 rounded hover:bg-gray-100'
                        >
                            Logout
                        </button>
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