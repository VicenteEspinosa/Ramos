import React, { useEffect, useState } from "react";
import style from "./pingList.module.css";
import axios from "axios";
import { getUser } from "../../utils";
import ReactScollableList from "react-scrollable-list";

const PingList = ({ loggedIn }) => {
  const [pings, updatePings] = useState([]);

  const errorMessage = () => {
    if (!loggedIn) return "Debes iniciar sesión para ver tus pings";
    if (pings.length === 0) return "Aun no tienes pings :(";
    return "";
  };

  useEffect(() => {
    const getPings = async () => {
        if (!loggedIn) {
            updatePings([]);
            return;
        }
      const response = await axios.get(`/pings/${getUser().id}`);
      updatePings(response.data);
    };
    getPings();
  }, [loggedIn]);

  const pingFormat = (pings) => {
    return pings.map((ping) => {
      return {
        id: ping.id,
        content:
          "Ping de " +
          ping.sender.username +
          " (Contacto: " +
          ping.sender.contact +
          ")",
      };
    });
  };

  return (
    <div className={style.general}>
      <div className={style.title}>Pings recibidos</div>
      <ReactScollableList listItems={pingFormat(pings)} />
      <div className={style.noPing}> {errorMessage()}</div>
    </div>
  );
};

export default PingList;
