import "./App.css";
import CustomTable from "./components/Table/CustomTable";
import Product from "./components/Product/Product";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import NavBar from "./components/NavBar/NavBar";

function App() {
  return (
    <div>
      <Router>
      <NavBar />
        <Routes>
          <Route
            path="/platos"
            exact
            element={<CustomTable type="courses" />}
          />
          <Route
            path="/ingredientes"
            exact
            element={<CustomTable type="ingredients" />}
          />
          <Route path="/" exact element={<CustomTable type="trays" />} />

          <Route path="/producto/:id/:type" element={<Product />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
