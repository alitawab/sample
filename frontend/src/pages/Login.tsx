import { useState } from "react";
import { useLogin } from "../hooks/useLogin";


export default function Login() {

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const { mutate, isPending } = useLogin();

    const handleSubmit = async(e: React.FormEvent) => {
        e.preventDefault();
        mutate({email, password});
    }

    return (
        <div className="max-w-sm mx-auto mt-20 p-4 border rounded-xl shadow">
            <h1 className="text-xl font-semibold mb-4">Login</h1>
            <form onSubmit={handleSubmit} className="flex flex-col gap-4">
                <input 
                type='email'
                placeholder='Enter Email'
                className="input input-bordered"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                />
                <input type='password'
                placeholder='Enter Password'
                className='input input-bordered'
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                />
                <button type="submit" className='btn btn-primary' disabled={isPending}>
                    Submit
                    {isPending ? 'Logging in...': 'Login'}
                </button>
            </form>
            
        </div>
    );
}