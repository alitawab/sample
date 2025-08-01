import ResturantCard from "../components/ResturantCard";
import { useResturnat } from "../hooks/useResturant";

export default function Home() {
    const { data, isLoading, isError } = useResturnat();
    

    if(isLoading) return <div className="text-center mt-100"> Loading Resturants...</div>
    if(isError) return <div className="text-center mt-100">Failed to Load Resturants...</div>

    return (
        <div className="p-4">
            <h1 className="text-2xl font-bold mb-6">Available Resturants</h1>
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
                {data.map((resturant:any)=>(
                    <ResturantCard 
                    key={resturant.resturant_id}
                    id = {resturant.resturant_id}
                    name={resturant.name}
                    image={resturant.logo_url}
                    address={resturant.address}
                    phone={resturant.phone}
                    open_hours={resturant.open_hours}
                    rating={resturant.rating}
                    tags={resturant.tags?.split(',') || []}
                    deliveryTime="30-40 mins"
                    />
                    // <div key={resturant.resturant_id} className="border rounded-xl p-4 shadow hover:shadow-md transition">
                    //     <img src={resturant.logo_url} alt={resturant.name} loading="lazy" className="h-32 object-contain mb-2" />
                    //     <h2 className="text-lg text-semibold">{resturant.name}</h2>
                    //     <p className="tetx-sm text-gray-600">{resturant.address}</p>
                    //     <p className="text-sm">{resturant.phone}</p>
                    //     <p className="text-sm">{resturant.open_hours}</p>
                    //     <p className="text-sm">{resturant.rating}</p>
                    //     {resturant.tags && resturant.tags.length > 0 && (
                    //         <div className="mt-2 flex flex-wrap gap-1">
                    //             {resturant.tags?.split(',').map((tag: string, i:number)=>(
                    //                 <span key={i} className="text-xs bg-gray-200 px-2 py-0.5 rounded-full">{tag}</span>
                    //             ))}
                    //         </div>
                    //     )}
                    // </div>
                ))}
            </div>
        </div>
    )
}