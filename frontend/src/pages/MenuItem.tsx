import { useParams } from "react-router-dom";
import { useMenuItemById } from "../hooks/useMenuItem"
import { useCart } from "../store/cart";


export default function MenuItem () {
    const {id} = useParams();
    const { data, isLoading, isError } = useMenuItemById(id);
    const { addToCart } = useCart();

    if(isLoading) return <div className="text-center mt-100">Item Loading...</div>
    if(isError) return <div className="text-center mt-100">Error Loading Item</div>

    return (
        <div className="p-6 max-w-xl mx-auto">
            <img src={`http://localhost:5000${data.image_url}`} alt={data.name} className="w-full h-64 object-cover rounded-xl mb-4" />
            <h1 className="text-3xl font-bold mb-2">{data.name}</h1>
            <p className="text-gray-700 mb-4">{data.description}</p>
            <p className="text-lg font-semibold mb-2">Rs - {data.price}</p>
            <button 
            onClick={() => addToCart({
                menuitem_id: data.menuitem_id,
                name: data.name,
                price: data.price,
                quantity: 1
            },data.resturant_id)}
            className="btn btn-sm mt-2 btn-primary">
                Add To Cart
            </button>
            <p className={`text-sm mt-2 ${data.is_available ? 'text-green-600' : 'text-red-600'}`}>
                {data.is_available ? 'Available':'Not-Available'}
            </p>
            
        </div>
    )
}