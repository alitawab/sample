import { useEffect, useState } from "react";
import L from "leaflet";
import 'leaflet/dist/leaflet.css'
import { MapContainer, Marker, TileLayer, useMap, useMapEvents } from "react-leaflet";

interface AddressModalProps {
    isOpen: boolean;
    onClose: () => void;
    onSave: (address: {id: number, text:string, latitude:number, longitude:number}) => void;
}

const markerIcon = new L.Icon({
    iconUrl: "https://unpkg.com/leaflet@1.7.1/dist/images/marker-icon.png",
    iconSize: [25,41],
    iconAnchor: [12,41],
});

function LocationMarker ({setPosition}: {setPosition: (pos:[number,number]) => void}){
    useMapEvents({
        click(e) {
            setPosition([e.latlng.lat, e.latlng.lng]);
        },
    });
    return null;
}

function RecenterMap({ center }: { center: [number, number] }) {
    const map = useMap();
    useEffect(() => {
        if (center) {
            map.setView(center, map.getZoom());
        }
    }, [center, map]);
    return null;
}

export default function AddressModal ({isOpen, onClose, onSave }: AddressModalProps) {
    const [form, setForm] = useState({house:'',street:'',area:''})
    const [position, setPosition]  = useState<[number,number]|null>(null)
    const [mapCenter, setMapCenter] = useState<[number,number]>([28.6139,77.2090])

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setForm({...form, [e.target.name]: e.target.value})
    }

    const isValid = form.house && form.street && form.area && position!==null;
    
    const handleSave = () => {
        if(!position) {alert("Please select a location for delivery"); return;}
        const fullAddress = `House No. ${form.house}, Street No. ${form.street}, Area. ${form.area}`;
        onSave({
            id:Date.now(),
            text: fullAddress,
            latitude: position[0],
            longitude: position[1],
        });
        setForm({house:"",street:"",area:""});
        onClose();
    };

        useEffect(() => {
        if(isOpen) {
            navigator.geolocation.getCurrentPosition(
                (pos) => {
                    const { latitude, longitude } = pos.coords;
                    setMapCenter([latitude,longitude]);
                    setPosition([latitude,longitude])
                },
                (err) => {
                    console.warn("Geolocation Error", err.message)
                },
                { enableHighAccuracy:true }
            );
        } else{
            setPosition(null);
            setForm({house:"",street:"",area:""})
        }
    },[isOpen])

    if (!isOpen) return null;

    return (
        <div className="fixed inset-0 bg-black bg-opacity-40 flex items-center justify-center z-50">
            <div className="bg-gray-600 rounded p-6 max-w-lg w-full">
                <h2 className="text-xl font-semibold mb-4">Add Delivery Address</h2>
                <div className="mb-4">
                    <MapContainer center={mapCenter} zoom={16} style={{ height:"300px", width: "100%" }} scrollWheelZoom={true}>
                        <TileLayer
                        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" 
                        attribution='&copy;<a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors'>
                        </TileLayer>
                        <RecenterMap center={mapCenter} />
                        {position && <Marker position={position} icon={markerIcon} />}
                        <LocationMarker setPosition={setPosition} />
                    </MapContainer>
                        {position && (
                            <p className="text-xs text-white mt-2">
                                Selected: Lat {position[0].toFixed(5)}, Lng {position[1].toFixed(5)}
                            </p>
                        )}
                        <p className="text-xs mt-2 text-gray-600">Tap On Map To Drop A Pin</p>
                </div>

                <div className="flex flex-col gap-3 mb-6">
                    <input name="house" type="text" placeholder="Enter House No." value={form.house} onChange={handleChange} className="input input-bordered w-full" />
                    <input name="street" type="text" placeholder="Enter Street No." value={form.street} onChange={handleChange} className="input input-bordered w-full" />
                    <input name="area" type="text" placeholder="Enter Area" value={form.area} onChange={handleChange} className="input input-bordered w-full" />
                </div>
                <div className="flex justify-end gap-3">
                    <button onClick={onClose} className="px-4 py-2 bg-gray-300 rounded hover:bg-gray-500">Cancel</button>
                    <button 
                    onClick={handleSave} 
                    disabled={!isValid} 
                    className={`px-4 py-2 rounded text-white ${isValid ? "bg-blue-600 hover:bg-blue-800" : "bg-gray-400 cursor-not-allowed"}`}
                        >
                        Confirm
                    </button>
                </div>
            </div>
        </div>
    )
}