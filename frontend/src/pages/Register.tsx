import { useState } from "react";
import { useRegister } from "../hooks/useRegister";


export default function Register() {
    const [form, setForm] = useState({
        name:'',
        email:'',
        phone:'',
        password:'',
    })

    const {mutate, isPending} = useRegister();

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value })
    }

    const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    mutate(form)
  }

  return (
    <div className="max-w-sm mx-auto mt-20 p-4 border rounded-xl shadow">
      <h1 className="text-xl font-semibold mb-4">Register</h1>
      <form onSubmit={handleSubmit} className="flex flex-col gap-4">
        <input name="name" type="text" placeholder="Name" value={form.name} onChange={handleChange} className="input input-bordered" />
        <input name="email" type="email" placeholder="Email" value={form.email} onChange={handleChange} className="input input-bordered" />
        <input name="phone" type="text" placeholder="Phone" value={form.phone} onChange={handleChange} className="input input-bordered" />
        <input name="password" type="password" placeholder="Password" value={form.password} onChange={handleChange} className="input input-bordered" />
        <button type="submit" disabled={isPending} className="btn btn-primary">
          {isPending ? 'Registering...' : 'Register'}
        </button>
      </form>
    </div>
  )
}