import { useState, useRef } from "react";
import { useNavigate } from "react-router-dom";
import toast from "react-hot-toast";
import { useRiderById, useRiderDelete, useRiderUpdate } from "../hooks/useRider";

export default function RiderProfile({rider_id}:{rider_id:number}) {
  const navigate = useNavigate();
  const { data: rider, isLoading, isError } = useRiderById(Number(rider_id));
  const { mutate: updateRider, isPending: isUpdating } = useRiderUpdate();
  const { mutate: deleteRider } = useRiderDelete();
  const fileRef = useRef<HTMLInputElement>(null);

  const [form, setForm] = useState({
    name: "",
    phone: "",
    vehicle_type: "",
    license_number: "",
    latitude: "",
    longitude:"",
});

  const [editing, setEditing] = useState(false);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setForm((prev) => ({ ...prev, [name]: value }));
  };

  const handleEditClick = () => {
    if (rider) {
      setForm({
        name: rider.name,
        phone: rider.phone,
        vehicle_type: rider.vehicle_type,
        license_number: rider.license_number,
        latitude: rider.current_location_lat.toString(),
        longitude: rider.current_location_lng.toString(),
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
    formData.append("phone", form.phone);
    formData.append("vehicle_type", form.vehicle_type);
    formData.append("license_number", form.license_number);
    formData.append("latitude", form.latitude);
    formData.append("longitude", form.longitude);

    updateRider(
      { id: Number(rider_id), formData },
      {
        onSuccess: () => {
          toast.success("Rider updated!");
          setEditing(false);
        },
        onError: () => toast.error("Update failed"),
      }
    );
  };

  const handleDelete = () => {
    if (confirm("Are you sure you want to delete this rider?")) {
      deleteRider(Number(rider_id), {
        onSuccess: () => {
          toast.success("Rider deleted");
          navigate("/");
        },
        onError: () => toast.error("Delete failed"),
      });
    }
  };

  if (isLoading) return <p>Loading...</p>;
  if (isError || !rider) return <p>Error loading rider.</p>;

  return (
    <div className="w-full flex flex-col mt-10 p-4 border shadow rounded-xl">
      <h1 className="text-2xl font-bold mb-4">Rider Profile</h1>

      {!editing ? (
        <>
          <h2 className="text-xl font-semibold"><strong className="text-xl">Name : </strong>{rider.name}</h2>
          <p><strong className="text-xl">Phone: </strong> {rider.phone}</p>
          <p><strong className="text-xl">Vehicle Type: </strong> {rider.vehicle_type}</p>
          <p><strong className="text-xl">License Number: </strong> {rider.license_number}</p>
          <p><strong className="text-xl">Latitude: </strong> {rider.current_location_lat}</p>
          <p><strong className="text-xl">Longitude: </strong> {rider.current_location_lng}</p>

          <div className="mt-6 flex gap-4">
            <button onClick={handleEditClick} className="btn btn-outline btn-info">Edit</button>
            <button onClick={handleDelete} className="btn btn-outline btn-error">Delete</button>
          </div>
        </>
      ) : (
        <form onSubmit={handleUpdate} className="space-y-4">
            <input name="name" value={form.name} onChange={handleChange} placeholder="Name" className="input input-bordered w-full" />
            <input name="phone" value={form.phone} onChange={handleChange} placeholder="Phone" className="input input-bordered w-full" />
            <input name="vehicle_type" value={form.vehicle_type} onChange={handleChange} placeholder="Vehicle Type" className="input input-bordered w-full" />
            <input name="license_number" value={form.license_number} onChange={handleChange} placeholder="License number" className="input input-bordered w-full" />
            <input name="latitude" value={form.latitude} onChange={handleChange} placeholder="Latitude" className="input input-bordered w-full" />
            <input name="longitude" value={form.longitude} onChange={handleChange} placeholder="Longitude" className="input input-bordered w-full" />



          <div className="flex gap-4 mt-4">
            <button type="submit" disabled={isUpdating} className="btn btn-primary">{isUpdating ? "Updating..." : "Update"}</button>
            <button type="button" onClick={handleCancelEdit} className="btn btn-secondary">Cancel</button>
          </div>
        </form>
      )}
    </div>
  );
}
