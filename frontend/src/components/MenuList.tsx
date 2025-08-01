import { Link } from "react-router-dom";

interface MenuItem {
    menuitem_id:number;
    name: string;
    description: string;
    price:number;
    image_url:string;
    is_available: boolean
}
interface Resturant {
    name:string;
    menu_items: MenuItem[];
}

export default function MenuList({resturant}:{resturant:Resturant}) {

    return (
        <div>
            <ul className="space-y-4">
                {resturant.menu_items.length === 0 ? (
                    <p>No Menu Items</p>
                ):(
                    resturant.menu_items.map((item)=>(
                        <div key={item.menuitem_id} className="flex flex-col space-y-4">
                            <Link to={`/item/${item.menuitem_id}`} className="shadow hover:shadow-md transition rounded overflow-hidden">
                                <div className="p-4 border flex items-start gap-4 min-h-[140px]">
                                    <img src={`http://127.0.0.1:5000${item.image_url}`} alt={item.name} className="w-28 h-28 object-cover rounded border" />
                                    <div className="lex-1 flex flex-col justify-between">
                                        <h2 className="text-lg font-medium">{item.name}</h2>
                                        <p className="text-sm text-gray-600 line-clamp-2">{item.description}</p>
                                        <p className="text-base font-semibold">Rs {item.price}</p>
                                        <p className={`text-xs ${item.is_available?'text-green-600':'text-red-600'}`}>
                                            {item.is_available ? 'Available':'Unavialabe'}
                                        </p>
                                    </div>
                                </div>
                            </Link>
                        </div>
                    ))

                )}
            </ul>
        </div>
    );
}