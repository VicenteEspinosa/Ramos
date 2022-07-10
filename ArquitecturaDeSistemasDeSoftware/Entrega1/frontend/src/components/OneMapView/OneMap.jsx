import "./oneMap.css";
import { MapContainer, TileLayer, useMapEvents } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import L from "leaflet";
import { useState } from "react";
import Login from "../Login/Login";
import PingList from "../PingList/PingList";
import { getUser } from "../../utils";
import UserInfo from "../Login/UserInfo/UserInfo";
import NewMarker from "../NewMarker/NewMarker";
import MarkerMapper from "../MarkerMapper/MarkerMapper";
import UserLocations from "../UserLocations/UserLocations";
import SearchUsers from "../SeachUsers/SearchUsers";

delete L.Icon.Default.prototype._getIconUrl;

L.Icon.Default.mergeOptions({
  iconRetinaUrl: require("leaflet/dist/images/marker-icon-2x.png"),
  iconUrl: require("leaflet/dist/images/marker-icon.png"),
  shadowUrl: require("leaflet/dist/images/marker-shadow.png"),
});

function OneMap({ setusersIds, updateShowMultipleMaps }) {
  const [fetchLocations, callFetchLocations] = useState(0);

  const checkSesion = () => {
    return getUser() ? true : false;
  };
  const [loggedIn, updateLogin] = useState(checkSesion());

  function LocationMarker() {
    const [position, setPosition] = useState(null);
    const map = useMapEvents({
      click(e) {
        map.flyTo(e.latlng, map.getZoom());
        setPosition(e.latlng);
      },
    });

    return position === null ? null : (
      <NewMarker
        position={position}
        fetchLocations={fetchLocations}
        callFetchLocations={callFetchLocations}
        mapObject={map}
        setPosition={setPosition}
        loggedIn={loggedIn}
      />
    );
  }
  return (
    <div className="App">
      <header className="App-header"></header>
      <div id="map">
        <MapContainer
          center={[-33.50007600916522, -70.6128686014563]}
          zoom={13}
        >
          <TileLayer
            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          />
          <MarkerMapper fetchLocations={fetchLocations} />
          <LocationMarker />
        </MapContainer>
        {loggedIn ? (
          <UserInfo updateLogin={updateLogin} />
        ) : (
          <Login updateLogin={updateLogin} />
        )}
        <PingList loggedIn={loggedIn} />
        <SearchUsers
          setusersIds={setusersIds}
          updateShowMultipleMaps={updateShowMultipleMaps}
        />
        <UserLocations loggedIn={loggedIn} />
      </div>
    </div>
  );
}

export default OneMap;
