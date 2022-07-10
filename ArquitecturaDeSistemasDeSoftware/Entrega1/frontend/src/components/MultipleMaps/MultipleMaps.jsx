import { MapContainer, TileLayer } from "react-leaflet";
import { useEffect, useState, useRef } from "react";
import PersonalizedMarker from "../PersonalizedMarker/PersonalizedMarker";
import L from "leaflet";
import "leaflet/dist/leaflet.css";
import style from "./multipleMaps.module.css";
import axios from "axios";

delete L.Icon.Default.prototype._getIconUrl;

L.Icon.Default.mergeOptions({
  iconRetinaUrl: require("leaflet/dist/images/marker-icon-2x.png"),
  iconUrl: require("leaflet/dist/images/marker-icon.png"),
  shadowUrl: require("leaflet/dist/images/marker-shadow.png"),
});


function MultipleMaps({ users_ids }) {
  const [locations, setLocations] = useState({});

  const getLocations = async (users_ids) => {
    const response = await axios.get(`locations/users/${users_ids}`);
    setLocations(response.data);
  };

  useEffect(() => {
    getLocations(users_ids);
  }, [users_ids]);

  return (
    <div className={style.general}>
      <div className={style.mapsContainer}>
        {Object.keys(locations).map((id, index) => (
          <div className={style.mapContainer} key={`${id}-container`}>
            <div
              className={index > 2 ? style.ownerBottom : style.owner}
              key={`${id}-owner`}
            >
              <p key={id}> Usuario: {locations[id].username} </p>
            </div>
            <div className={style.mapHolder} key={`${id}-map`}>
              <MapContainer
                className={index > 2 ? style.mapBottom : style.map}
                center={[-33.50007600916522, -70.6128686014563]}
                zoom={13}
                key={id}
              >
                <TileLayer
                  key={id}
                  attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                  url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                />
                {locations[id]["locations"].map((location_data) => (
                  <PersonalizedMarker
                    key={location_data.id}
                    id={location_data.id}
                    name={location_data.name}
                    owner={location_data.user}
                    position={[location_data.lat, location_data.long]}
                    hidePing={true}
                  />
                ))}
              </MapContainer>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default MultipleMaps;
