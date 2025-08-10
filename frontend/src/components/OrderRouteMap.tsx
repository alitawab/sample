import { useEffect, useRef } from "react";
import L from 'leaflet'
import 'leaflet-routing-machine';
import { MapContainer, TileLayer, useMap } from "react-leaflet";

interface Props {
    destination: {lat:number, lng:number}
}

function Routing({destination}: Props){
    const map =useMap()
    const routingControlRef = useRef<any>(null);

    useEffect(()=>{
        if(!navigator.geolocation) return;
        navigator.geolocation.getCurrentPosition(
            (position) => {
                const riderLocation = L.latLng(position.coords.latitude, position.coords.longitude);
                const deliveryLocation = L.latLng(destination.lat, destination.lng);

                    const control = L.Routing.control({
                    waypoints: [riderLocation, deliveryLocation],
                    routeWhileDragging: false,
                    show: false,
                }).addTo(map)
                routingControlRef.current = control;
            },
            (error) => {
                console.error("Could not get current position",error)
            }
        );
        return () => {
            if(routingControlRef.current) {
                map.removeControl(routingControlRef.current)
                routingControlRef.current = null;
            }
        };
    },[map,destination])
    return null;
}

export default function OrderRouteMap ({destination}: Props) {
    return (
        <MapContainer center={[destination.lat,destination.lng]} zoom={13} style={{height:'300px',width:'100%'}}>
            <TileLayer attribution='&copy; <a href="https://osm.org/copyright">OpenStreetMap</a>' 
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
            <Routing destination={destination} />
        </MapContainer>
    );
}