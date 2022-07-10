import React, { useEffect, useState } from "react";
import style from "./newMarker.module.css";
import { Marker, Popup } from "react-leaflet";
import axios from "axios";
import { getUser } from "../../utils";

const NewMarker = ({
  position,
  fetchLocations,
  callFetchLocations,
  mapObject,
  setPosition,
  loggedIn,
}) => {
  const [query_name, updateName] = useState("");
  const [latitude, updateLatitude] = useState(position.lat);
  const [longitude, updateLongitude] = useState(position.lng);

  useEffect(() => {
    mapObject.flyTo({ lat: latitude, lng: longitude }, mapObject.getZoom());
    setPosition({ lat: latitude, lng: longitude });
    position = { lat: latitude, lng: longitude };
  }, [latitude, longitude]);

  useEffect(() => {
    updateLatitude(position.lat);
    updateLongitude(position.lng);
  }, [position]);

  const newPosition = async () => {
    await axios.post("/location/create", {
      lat: position.lat,
      long: position.lng,
      name: query_name,
      user_id: getUser().id,
    });
    callFetchLocations(fetchLocations + 1);
  };
  return (
    <div className={style.general}>
      <Marker opacity={0.5} position={position}>
        <Popup>
          <label className={style.label}>
            <input
              className={style.input}
              placeholder="Nombre"
              name="name"
              value={query_name}
              onChange={(e) => updateName(e.target.value)}
            ></input>
          </label>
          <label className={style.label}>
            <div className={style.coords}>
              <div className={style.coord}>
                <input
                  className={style.input}
                  placeholder="Latitud"
                  name="lat"
                  value={latitude}
                  onChange={(e) => updateLatitude(e.target.value)}
                ></input>
              </div>
              <div className={style.coord}>
                <input
                  className={style.input}
                  placeholder="Longitud"
                  name="long"
                  value={longitude}
                  onChange={(e) => updateLongitude(e.target.value)}
                ></input>
              </div>
            </div>
          </label>
          <div className={style.label}>
            {loggedIn ? (
              <button className={style.createButton} onClick={newPosition}>
                Crear nueva ubicación
              </button>
            ) : <p>Inicia sesion para crear</p>}
          </div>
        </Popup>
      </Marker>
    </div>
  );
};

export default NewMarker;
