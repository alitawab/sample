
export interface User {
    user_id: number
    resturant_id:number
    name: string
    email: string
    phone: string
    role: 'user'| 'rider' | 'resturant'
}

export interface LoginResponse {
  token: string
  user: User
}
