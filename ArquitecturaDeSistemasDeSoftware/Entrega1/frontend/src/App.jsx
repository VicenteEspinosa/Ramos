import OneMap from "./components/OneMapView/OneMap";
import MultipleMaps from "./components/MultipleMaps/MultipleMaps";
import { useState } from "react";

function App() {
  const [usersIds, setusersIds] = useState(0);
  const [showMultipleMaps, updateShowMultipleMaps] = useState(false);
  return (
    <div className="App">
      {showMultipleMaps ? (
        <MultipleMaps users_ids={usersIds} />
      ) : (
        <OneMap setusersIds={setusersIds} updateShowMultipleMaps={updateShowMultipleMaps} />
      )}
    </div>
  );
}

export default App;
