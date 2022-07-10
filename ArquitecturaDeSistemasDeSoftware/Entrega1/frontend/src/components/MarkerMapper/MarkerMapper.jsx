import axios from "axios";
import React, { useEffect, useState } from "react";
import PersonalizedMarker from "../PersonalizedMarker/PersonalizedMarker";

const MarkerMapper = ({ fetchLocations }) => {
  const [locations, updatelocations] = useState([]);

  useEffect(() => {
    const getLocations = async () => {
      const response = await axios.get("/locations");
      updatelocations(response.data);
    };
    getLocations();
  }, [fetchLocations]);

  return (
    <div>
      {locations.map((location) => (
        <PersonalizedMarker
          key={location.id}
          id={location.id}
          name={location.name}
          owner={location.user}
          position={[location.lat, location.long]}
        />
      ))}
    </div>
  );
};
export default MarkerMapper;
