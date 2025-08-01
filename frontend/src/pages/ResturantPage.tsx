import { useParams } from "react-router-dom";
import { useResturantById } from "../hooks/useResturant";
import MenuList from "../components/MenuList";

export default function ResturantPage() {
    const {id}  = useParams();
    const { data, isLoading, isError } = useResturantById(id)

    if(isLoading) return <div className="text-center mt-100">Resturant Menu Loading...</div>
    if(isError) return <div className="text-center mt-100">Error Loading Menu Items...</div>
    return(
        <div className="p-4">
            <h2 className="text-xl font-semibold mt-6 mb-4">{data.name} - Menu</h2>
            <div>
                <MenuList 
                resturant={data}
                />
            </div>

        </div>
        
    )
}