import { QueryClient, useMutation, useQuery, useQueryClient } from "@tanstack/react-query"
import { addMenuItem, deleteMenuItem, getMenuItemById, getMenuItemByResturantId, getMenuItems, updateMenuItem } from "../services/menuitem"
import toast from "react-hot-toast"


export const useMenuItem = () => {
    return useQuery({
        queryKey: ['MenuItems'],
        queryFn: getMenuItems,
    })
}

export const useMenuItemById = (id: any) => {
    return useQuery({
        queryKey:['MenuItems',id],
        queryFn:() => getMenuItemById(id)
    })
}


export const useMenuItemAdd = () => {
    const queryClient = useQueryClient();
    return useMutation({
        mutationFn: addMenuItem,
        onSuccess: (_, variable) => {
            const resturant_id = Number(variable.get("resturant_id"));
            queryClient.invalidateQueries({queryKey:['MenuItems',resturant_id]});
            toast("Item Stored Succesfully")    
        }
    })
}

export const useMenuItemDelete = () => {
    const queryClient = useQueryClient();
    return useMutation({
        mutationFn:({menuitem_id, resturant_id}: {menuitem_id:number; resturant_id:number}) => 
            deleteMenuItem(menuitem_id),
        onSuccess: (_,variable) => {
            queryClient.invalidateQueries({queryKey:['MenuItems',variable.resturant_id]})
            toast.success("Item Deleted")
        }
    })
}

export const useMenuItemUpdate = () => {
    const queryClient = useQueryClient();
    return useMutation({
        mutationFn: ({id, formData, resturant_id}:{id:any; formData:FormData; resturant_id:number}) =>  
            updateMenuItem(id , formData),
        onSuccess: (_, { resturant_id }) => {
            queryClient.invalidateQueries({queryKey:['MenuItems', resturant_id]});
            toast("Item Updated Successfully");


        }
    })
}


export const useMenuItemByResturantId = (id: any) => {
    return useQuery({
        queryKey:['MenuItems',id],
        queryFn:() => getMenuItemByResturantId(id),
        enabled: !!id,

    })
}
