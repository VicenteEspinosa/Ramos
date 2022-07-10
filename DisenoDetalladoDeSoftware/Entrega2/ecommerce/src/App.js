import "./App.css";
import Purchases from "./components/Purchases/Purchases";
import Cupons from "./components/Cupons/Cupons";
import { useState } from "react";

function App() {
  const [showPurchases, setShowPurchases] = useState(true);
  return (
    <div className="App">
      {showPurchases ? <Purchases /> : <Cupons />}
      <button onClick={() => setShowPurchases(!showPurchases)}>
        Ver {showPurchases ? "Cupones" : "Compras"}
      </button>
    </div>
  );
}

export default App;
