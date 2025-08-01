import { Link } from "react-router-dom";


interface ResturantCardProp {
    id: number;
    name: string;
    image: string;
    address: string;
    phone: string;
    open_hours: string;
    rating: string;
    tags: string[];
    deliveryTime: string;
}

export default function ResturantCard({id, name, image, address, phone, open_hours, rating, tags, deliveryTime}: ResturantCardProp) {
    return (
        <div className="border rounded-xl p-2 shadow hover:shadow-md transition">
            <img src={`http://localhost:5000${image}`} alt={name} className="w-52 h-52 object-contain p-2 rounded mb-2 mx-auto"/>
            <h2 className="text-lg text-semibold">{name}</h2>
            <p className="tetx-sm text-gray-600">{address}</p>
            <p className="text-sm">{phone}</p>
            <p className="text-sm">{open_hours}</p>
             {tags && tags.length > 0 && (
                    <div className="mt-2 flex flex-wrap gap-1">
                        {tags.map((tag: string, i:number)=>(
                            <span key={i} className="text-xs bg-indigo-500 px-2 py-0.5 rounded-full">{tag}</span>
                        ))}
                    </div>
            )}
            <p className="mt-2 text-sm text-semibold">Delivery in {deliveryTime}</p>                
            <Link to={`/resturant/${id}`}>
                <button className="mt-4 btn btn-primary w-full">View Menu</button>
            </Link>
        </div>
    );
}