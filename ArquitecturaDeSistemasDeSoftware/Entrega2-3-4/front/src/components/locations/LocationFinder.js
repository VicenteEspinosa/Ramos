import { useState } from "react";
import axios from '../../api/axios';
import { MapContainer, TileLayer, Marker, Popup  } from 'react-leaflet'
import { Icon } from "leaflet";
import './leaflet.css';

// fill a form for five usernames and get user's locations
export default function LocationFinder() {
    const [locations1, setLocations1] = useState([]);
    const [locations2, setLocations2] = useState([]);
    const [locations3, setLocations3] = useState([]);
    const [locations4, setLocations4] = useState([]);
    const [locations5, setLocations5] = useState([]);
    const [username, setUsername] = useState('');
    const [username2, setUsername2] = useState('');
    const [username3, setUsername3] = useState('');
    const [username4, setUsername4] = useState('');
    const [username5, setUsername5] = useState('');
    const [error, setError] = useState('');

    const handleSubmit = (event) => {
        event.preventDefault();
        axios.get('/locations/user/' + username)
            .then(response => {
                setLocations1(response.data);
            })
            .catch(error => {
                setError(error.message);
            });
    }

    const handleSubmit2 = (event) => {
        event.preventDefault();
        axios.get('/locations/user/' + username2)
            .then(response => {
                setLocations2(response.data);
            })
            .catch(error => {
                setError(error.message);
            });
    }

    const handleSubmit3 = (event) => {
        event.preventDefault();
        axios.get('/locations/user/' + username3)
            .then(response => {
                setLocations3(response.data);
            })
            .catch(error => {
                setError(error.message);
            });
    }

    const handleSubmit4 = (event) => {
        event.preventDefault();
        axios.get('/locations/user/' + username4)
            .then(response => {
                setLocations4(response.data);
            })
            .catch(error => {
                setError(error.message);
            }
            );
    }

    const handleSubmit5 = (event) => {
        event.preventDefault();
        axios.get('/locations/user/' + username5)
            .then(response => {
                setLocations5(response.data);
            })
            .catch(error => {
                setError(error.message);
            });
    }

    const loc = new Icon({
        iconUrl: "https://www.pngall.com/wp-content/uploads/2017/05/Map-Marker-Free-Download-PNG.png",
        iconSize: [25, 25]
      });

    return (
        <div>
            <h1 align="center" >DONT SEARCH USERS WITHOUT LOCATIONS!!! IT WILL CRASH!!!</h1>
            <form onSubmit={handleSubmit}>
                <label>
                    Username: 
                    <input type="text" value={username} onChange={e => setUsername(e.target.value)} />
                </label>
                <input type="submit" value="Submit" />
            </form>
            <form onSubmit={handleSubmit2}>
                <label>
                    Username: 
                    <input type="text" value={username2} onChange={e => setUsername2(e.target.value)} />
                </label>
                <input type="submit" value="Submit" />
            </form>
            <form onSubmit={handleSubmit3}>
                <label>
                    Username: 
                    <input type="text" value={username3} onChange={e => setUsername3(e.target.value)} />
                </label>
                <input type="submit" value="Submit" />
            </form>
            <form onSubmit={handleSubmit4}>
                <label>
                    Username: 
                    <input type="text" value={username4} onChange={e => setUsername4(e.target.value)} />
                </label>
                <input type="submit" value="Submit" />
            </form>
            <form onSubmit={handleSubmit5}>
                <label>
                    Username: 
                    <input type="text" value={username5} onChange={e => setUsername5(e.target.value)} />
                </label>
                <input type="submit" value="Submit" />
            </form>
            <div id="map">
                <MapContainer center={[70, 30]} zoom={3}>
                    <TileLayer
                        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                        attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                    />
                    {locations1.map(location => (
                        <Marker key={location._id} position={[location[0].location.coordinates[0], location[0].location.coordinates[1]]} icon={ loc }>
                            <Popup>
                                <div>{location.name}</div>
                                <div>{username}</div>
                            </Popup>
                        </Marker>
                    ))}
                    {locations2.map(location => (
                        <Marker key={location._id} position={[location[0].location.coordinates[0], location[0].location.coordinates[1]]} icon={ loc }>
                            <Popup>
                                <div>{location.name}</div>
                                <div>{username2}</div>
                            </Popup>
                        </Marker>
                    ))}
                    {locations3.map(location => (
                        <Marker key={location._id} position={[location[0].location.coordinates[0], location[0].location.coordinates[1]]} icon={ loc }>
                            <Popup>
                                <div>{location.name}</div>
                                <div>{username3}</div>
                            </Popup>
                        </Marker>
                    ))}
                    {locations4.map(location => (
                        <Marker key={location._id} position={[location[0].location.coordinates[0], location[0].location.coordinates[1]]} icon={ loc }>
                            <Popup>
                                <div>{location.name}</div>
                                <div>{username4}</div>
                            </Popup>
                        </Marker>
                    ))}
                    {locations5.map(location => (
                        <Marker key={location._id} position={[location[0].location.coordinates[0], location[0].location.coordinates[1]]} icon={ loc }>
                            <Popup>
                                <div>{location.name}</div>
                                <div>{username5}</div>
                            </Popup>
                        </Marker>
                    ))}
                </MapContainer>
            </div>
            <div>
                {error && <p>{error}</p>}
            </div>
        </div>
    );
}


