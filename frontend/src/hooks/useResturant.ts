import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query"
import { getResturant, getResturantById, updateRestaurant, deleteRestaurant } from "../services/resturant"


export const useResturnat = () => {
    return useQuery({
        queryKey: ['resturant'],
        queryFn: getResturant,
    })
}

export const useResturantById = (id: any) => {
    return useQuery({
        queryKey:['resturant',id],
        queryFn: () => getResturantById(id),
    })
}

export const useRestaurantUpdate = () => {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: ({ id, formData }: { id: number; formData: FormData }) => updateRestaurant(id, formData),
    onSuccess: (_, { id }) => queryClient.invalidateQueries({ queryKey: ['resturant', id] }),
  });
};

export const useRestaurantDelete = () => {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: (id: number) => deleteRestaurant(id),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['resturant'] }),
  });
};

