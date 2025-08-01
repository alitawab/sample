import { useRef, useState } from "react";
import { useMenuItemAdd, useMenuItemByResturantId, useMenuItemDelete, useMenuItemUpdate } from "../hooks/useMenuItem";


export default function MenuManager({resturant_id}:{resturant_id:number}) {
    const [form, setForm] = useState({
        name:"",
        description:"",
        price: "" ,
        image: null as File | null,
        is_available: true,
    });

    const fileInputRef = useRef<HTMLInputElement| null>(null);
    const [editId, setEditId] = useState<number|null>(null);
    const {data:items=[], isLoading, isError} = useMenuItemByResturantId(resturant_id);
    const {mutate, isPending} = useMenuItemAdd();
    const {mutate:mutateDelete} = useMenuItemDelete();
    const {mutate:mutateUpdate, isPending:isUpdating} = useMenuItemUpdate();
    

    const resetForm = () => {
        setForm({
                    name: "",
                    description: "",
                    price: "",
                    image: null,
                    is_available: true,
                });
        setEditId(null);
        if(fileInputRef.current){
            fileInputRef.current.value=""
        }
    }
    const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement >) => {
        const { name, value, type} = e.target;
        
        const updatedValue = type === "checkbox"
        ? (e.target as HTMLInputElement).checked
        : value;

        setForm((prev) => ({
            ...prev, [name]: updatedValue
        }));
    }

    const handleImageChange = (e:React.ChangeEvent<HTMLInputElement>) => {
        if(e.target.files?.[0]){
            setForm((prev) => ({...prev, image: e.target.files![0]}));
        }

    }
    const handleSubmit = async(e:React.FormEvent) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append("resturant_id",String(resturant_id))
        formData.append("name",form.name);
        formData.append("description",form.description);
        formData.append("price",String(form.price));
        formData.append("is_available",String(form.is_available));
        if(form.image) {
            formData.append("image",form.image)
        }

        if(editId){
            mutateUpdate({ id:editId , formData, resturant_id },{
                onSuccess: () => {
                    resetForm();
                },
            });
        } else {
            mutate(formData, {
                onSuccess: () => {
                    resetForm();
                },
            })
        }
    }
    const handleEdit = (item:any) => {
        setForm({
            name:item.name,
            description:item.description,
            price:item.price,
            image:null,
            is_available:item.is_available,
        });
        setEditId(item.menuitem_id);
    }

    const handleDelete = (menuitem_id:number) => {
        if(confirm("Are you sure you want to delete this item")){
            mutateDelete({menuitem_id,resturant_id})
        }
    }


    return (
        <div>
            <h2 className="text-xl font-bold mb-4">Manage Menu Items</h2>
            
            {isLoading && <p className="text-gray-500">Loading...</p>}
            {isError && <p className="text-red-500">Error loading menu items</p>}

            {/* Form to add new item */}
            <form onSubmit={handleSubmit} className="space-y-4 mb-10">
                <input name="name" value={form.name} onChange={handleChange} placeholder="Item Name" className="input input-bordered w-full" />
                <textarea name="description" value={form.description} onChange={handleChange} placeholder="Description" className="textarea textarea-bordered w-full" />
                <input name="price" type="number" value={form.price} onChange={handleChange} placeholder="Price" className="input input-bordered w-full" />
                <input type="file" ref={fileInputRef} onChange={handleImageChange} className="file-input file-input-bordered" />
                <label className="flex items-center gap-2">
                <input type="checkbox" name="is_available" checked={form.is_available} onChange={handleChange} className="checkbox" />
                    Available
                </label>
                <button type="submit" className="btn btn-primary" disabled={isPending}>
                    {editId ? (isPending ? 'Updating...' : 'Update Item') : (isPending ? 'Adding...' : 'Add Menu Item')}
                </button>
            </form>

      {/* List existing items */}
      {items.length === 0 ? (
        <p className="text-center text-red-500">No menu items added yet.</p>
    ):(
        <div className="flex flex-col space-y-4">
            {items.map((item:any) => (
                <div key={item.menuitem_id} className="p-2 border shadow flex gap-4 items-center">
                    <img src={`http://localhost:5000${item.image_url}`} alt={item.name} className="w-28 h-28 object-cover rounded" />
                    <h3 className="text-lg font-semibold">{item.name}</h3>
                    <p className="text-sm">{item.description}</p>
                    <p className="font-medium">Rs. {item.price}</p>
                    <p className="text-xs">Status: {item.is_available ? "Available" : "Unavailable"}</p>
                    <button
                    onClick={() => handleEdit(item)}
                    className="btn btn-sm btn-outline btn-info"
                    >
                        Edit
                    </button>
                    <button
                    onClick={() => handleDelete(item.menuitem_id)}
                    className="btn btn-sm btn-outline btn-error"
                    >
                        Delete
                    </button>
                </div>
            ))}
        </div>
    )}
    </div>
    )
}
