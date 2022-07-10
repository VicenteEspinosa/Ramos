import React, { useEffect, useState } from "react";
import style from "./userLocations.module.css";
import axios from "axios";
import { getUser } from "../../utils";
import ReactScollableList from "react-scrollable-list";

const UserLocations = ({ loggedIn }) => {
  const [locations, updateLocations] = useState([]);

  const errorMessage = () => {
    if (!loggedIn) return "Debes iniciar sesión para ver tus ubicaciones";
    if (locations.length === 0) return "Aun no tienes ubicaciones";
    return "";
  };

  useEffect(() => {
    const getLocations = async () => {
      if (!loggedIn) {
        updateLocations([]);
        return;
      }
      const response = await axios.get(`/locations/${getUser().id}`);
      updateLocations(response.data);
    };
    getLocations();
  }, [loggedIn]);

  const locationsFormat = (locations) => {
    return locations.map((location) => {
      return {
        id: locations.id,
        content: (
          <div>
            <p>
              {location.name} [{location.lat.toFixed(2)},{" "}
              {location.long.toFixed(2)}]
            </p>
          </div>
        ),
      };
    });
  };

  return (
    <div className={style.general}>
      <div className={style.title}>Tus Ubicaciones</div>
      <ReactScollableList listItems={locationsFormat(locations)} />
      <div className={style.noLocation}>{errorMessage()}</div>
    </div>
  );
};

export default UserLocations;
