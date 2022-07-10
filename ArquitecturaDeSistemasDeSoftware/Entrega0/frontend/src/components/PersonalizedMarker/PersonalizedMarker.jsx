import React, { useState } from "react";
import style from "./personalizedMarker.module.css";
import { Marker, Popup } from "react-leaflet";
import { getUser } from "../../utils";
import axios from "axios";

const PersonalizedMarker = ({ position, name, owner }) => {
  const [pinged, setPinged] = useState(false);

  const pingUser = async () => {
    try {
      await axios.post("ping/create", {
        sender_id: getUser().id,
        receiver_id: owner.id,
      });
      setPinged(true);
    } catch (_) {}
  };
  const showButton = () => {
    if (pinged) return false;
    if (getUser()) {
      if (getUser().id !== owner.id) return true;
    }
    return false;
  };

  const alertMessages = () => {
    if (getUser()) {
      if (getUser().id === owner.id) return "Esta ubicación es tuya";
      return null;
    } else {
      return "Debes iniciar sesion";
    }
  };
  return (
    <div className={style.general}>
      <Marker className={style.customMarker} position={position}>
        <Popup>
          <div className={style.name}> {name} </div>
          <br />
          <div className={style.owner}> {owner.username} </div>
          <div className={style.buttonHolder}>
            {pinged ? "Ping enviado!" : null}
            {showButton() ? (
              <button className={style.button} onClick={pingUser}>
                Enviar Ping
              </button>
            ) : null}
            {alertMessages()}
          </div>
        </Popup>
      </Marker>
    </div>
  );
};

export default PersonalizedMarker;
