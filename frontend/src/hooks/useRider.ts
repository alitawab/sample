import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query"
import { deleteRider, getRider, getRiderById, getRiderByUserId, updateRider } from "../services/rider"
import type { Rider } from "../types/rider"


export const useRider = () => {
    return useQuery({
        queryKey: ['rider'],
        queryFn: getRider,
    })
}

export const useRiderById = (id: number) => {
    return useQuery<Rider>({
        queryKey:['rider',id],
        queryFn: () => getRiderById(id)
    })
}

export const useRiderUpdate = () => {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: ({ id, formData }: { id: number; formData: FormData }) => updateRider(id, formData),
    onSuccess: (_, { id }) => queryClient.invalidateQueries({ queryKey: ["rider", id] }),
  });
};

export const useRiderDelete = () => {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: (id: number) => deleteRider(id),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ["rider"] }),
  });
};

