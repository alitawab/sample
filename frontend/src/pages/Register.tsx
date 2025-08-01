import { useState } from "react";
import { useRegister } from "../hooks/useRegister";


export default function Register() {
    const [form, setForm] = useState({
        name:'',
        email:'',
        phone:'',
        password:'',
        role:'user',
        // conditional fields resturant
        resturant_name:'',
        resturant_address:'',
        logo_url: null as File | null,
        rating:'',
        tags:'',
        open_hours:'',
        //conditiona; fields for rider
        vehicle_type:'',
        liscence_number:'',
    })

    const {mutate, isPending} = useRegister();

    const handleChange = (e: React.ChangeEvent<HTMLInputElement|HTMLSelectElement>) => {
      const { name, value} = e.target;
      setForm(prev => ({ ...prev, [name]: value }));
    }
    
    const handleImageChange = (e:React.ChangeEvent<HTMLInputElement>) => {
      if (e.target.files?.[0]) {
        setForm((prev) => ({
          ...prev,
          logo_url: e.target.files![0],
        }));
      }
    }

    const handleSubmit = (e: React.FormEvent) => {
      e.preventDefault()
      const formData = new FormData();
      formData.append('name', form.name);
      formData.append('email', form.email);
      formData.append('phone', form.phone);
      formData.append('password', form.password);
      formData.append('role', form.role);
      if (form.role === 'resturant'){
        formData.append('resturant_name', form.resturant_name);
        formData.append('resturant_address', form.resturant_address);
        formData.append('tags', form.tags);
        formData.append('open_hours', form.open_hours);
        if (form.logo_url) {
          formData.append('image', form.logo_url);
        }
      }
      if(form.role === 'rider'){
        formData.append('vehicle_type', form.vehicle_type);
        formData.append('license_number', form.liscence_number);
  
      }
      mutate(formData)
    }
  

  return (
    <div className="max-w-sm mx-auto mt-20 p-4 border border-black rounded-xl shadow">
      <h1 className="text-xl font-semibold mb-4">Register</h1>
      <form onSubmit={handleSubmit} className="flex flex-col gap-4">
        <input name="name" type="text" placeholder="Name" value={form.name} onChange={handleChange} className="input input-bordered" />
        <input name="email" type="email" placeholder="Email" value={form.email} onChange={handleChange} className="input input-bordered" />
        <input name="phone" type="text" placeholder="Phone" value={form.phone} onChange={handleChange} className="input input-bordered" />
        <input name="password" type="password" placeholder="Password" value={form.password} onChange={handleChange} className="input input-bordered" />
        <select name="role" value={form.role} onChange={handleChange} className="select select-bordered">
          <option value='user'>User</option>
          <option value='resturant'>Resturant</option>
          <option value='rider'>Rider</option>
        </select>
        {form.role === 'resturant' && (
          <>
          <input name="resturant_name" type="text" placeholder="Restaurant Name" value={form.resturant_name} onChange={handleChange} className="input input-bordered"/>
          <input name="resturant_address" type="text" placeholder="Restaurant Address" value={form.resturant_address} onChange={handleChange} className="input input-bordered"/>
          <input name="logo_url" type="file" placeholder="Restaurant Logo" onChange={handleImageChange} className="file-input file-input-bordered"/>
          <input name="tags" type="text" placeholder="Restaurant Tags (Cheese,Burger,Spicy)" value={form.tags} onChange={handleChange} className="input input-bordered"/>
          <input name="open_hours" type="text" placeholder="Open Hours 10:00 AM - 10:00 PM " value={form.open_hours} onChange={handleChange} className="input input-bordered"/>
          </>
        )}
        {form.role === 'rider' && (
          <>
          <input name="vehicle_type" type="text" placeholder="Vehicle Type" value={form.vehicle_type} onChange={handleChange} className="input input-bordered"/>
          <input name="license_number" type="text" placeholder="License Number" value={form.liscence_number} onChange={handleChange} className="input input-bordered"/>
          </>
        )}
        <button type="submit" disabled={isPending} className="btn btn-primary">
          {isPending ? 'Registering...' : 'Register'}
        </button>
      </form>
    </div>
  )
}