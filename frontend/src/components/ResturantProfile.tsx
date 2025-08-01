import { useState, useRef } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { useResturantById, useRestaurantUpdate, useRestaurantDelete } from "../hooks/useResturant";
import toast from "react-hot-toast";

export default function RestaurantProfile({resturant_id}:{resturant_id:number}) {
  const { id } = useParams();
  const navigate = useNavigate();
  const { data: restaurant, isLoading, isError } = useResturantById(Number(resturant_id));
  const { mutate: updateRestaurant, isPending: isUpdating } = useRestaurantUpdate();
  const { mutate: deleteRestaurant } = useRestaurantDelete();
  const fileRef = useRef<HTMLInputElement>(null);

  const [form, setForm] = useState({
    name: "",
    address: "",
    phone: "",
    open_hours: "",
    tags: "",
    image: null as File | null,
  });

  const [editing, setEditing] = useState(false);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setForm((prev) => ({ ...prev, [name]: value }));
  };

  const handleImageChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files?.[0]) {
      setForm((prev) => ({ ...prev, image: e.target.files![0] }));
    }
  };

  const handleEditClick = () => {
    if (restaurant) {
      setForm({
        name: restaurant.name,
        address: restaurant.address,
        phone: restaurant.phone,
        open_hours: restaurant.open_hours,
        tags: restaurant.tags,
        image: null,
      });
      setEditing(true);
    }
  };

  const handleCancelEdit = () => {
    setEditing(false);
    if (fileRef.current) fileRef.current.value = "";
  };

  const handleUpdate = (e: React.FormEvent) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("name", form.name);
    formData.append("address", form.address);
    formData.append("phone", form.phone);
    formData.append("open_hours", form.open_hours);
    formData.append("tags", form.tags);
    if (form.image) formData.append("image", form.image);

    updateRestaurant(
      { id: Number(id), formData },
      {
        onSuccess: () => {
          toast.success("Restaurant updated!");
          setEditing(false);
        },
        onError: () => toast.error("Update failed"),
      }
    );
  };

  const handleDelete = () => {
    if (confirm("Are you sure you want to delete this restaurant?")) {
      deleteRestaurant(Number(id), {
        onSuccess: () => {
          toast.success("Restaurant deleted");
          navigate("/");
        },
        onError: () => toast.error("Delete failed"),
      });
    }
  };

  if (isLoading) return <p>Loading...</p>;
  if (isError || !restaurant) return <p>Error loading restaurant.</p>;

  return (
    <div className="w-full flex flex-col items-center text-center mt-10 p-4 border shadow rounded-xl">
      <h1 className="text-2xl font-bold mb-4">Restaurant Profile</h1>

      {!editing ? (
        <>
          <img src={`http://localhost:5000${restaurant.logo_url}`} alt={restaurant.name} className="w-48 h-48 object-cover rounded mb-4" />
          <h2 className="text-xl font-semibold">{restaurant.name}</h2>
          <p><strong>Address:</strong> {restaurant.address}</p>
          <p><strong>Phone:</strong> {restaurant.phone}</p>
          <p><strong>Hours:</strong> {restaurant.open_hours}</p>
          <p><strong>Tags:</strong> {restaurant.tags}</p>

          <div className="mt-6 flex gap-4">
            <button onClick={handleEditClick} className="btn btn-info">Edit</button>
            <button onClick={handleDelete} className="btn btn-error">Delete</button>
          </div>
        </>
      ) : (
        <form onSubmit={handleUpdate} className="space-y-4">
          <input name="name" value={form.name} onChange={handleChange} placeholder="Name" className="input input-bordered w-full" />
          <input name="address" value={form.address} onChange={handleChange} placeholder="Address" className="input input-bordered w-full" />
          <input name="phone" value={form.phone} onChange={handleChange} placeholder="Phone" className="input input-bordered w-full" />
          <input name="open_hours" value={form.open_hours} onChange={handleChange} placeholder="Open Hours" className="input input-bordered w-full" />
          <input name="tags" value={form.tags} onChange={handleChange} placeholder="Tags" className="input input-bordered w-full" />
          <input type="file" ref={fileRef} onChange={handleImageChange} className="file-input file-input-bordered" />

          <div className="flex gap-4 mt-4">
            <button type="submit" disabled={isUpdating} className="btn btn-primary">{isUpdating ? "Updating..." : "Update"}</button>
            <button type="button" onClick={handleCancelEdit} className="btn btn-secondary">Cancel</button>
          </div>
        </form>
      )}
    </div>
  );
}
