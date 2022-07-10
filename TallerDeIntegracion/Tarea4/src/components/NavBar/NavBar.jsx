import React from "react";
import { Link } from "react-router-dom";
import style from "./NavBar.module.css";
import { useState } from "react";
import Select from "react-select/";
import axios from "axios";

export default function NavBar() {
  const [searchName, setSearchName] = useState("");
  const [options, setOptions] = useState([]);
  const NavStyle = {
    color: "black",
    textDecoration: "none",
  };

  const customStyles = {
    container: provided => ({
      ...provided,
      width: 300
    })
  };

  const updateSearchInput = async (value) => {
    setSearchName(value);
    setOptions([]);
    if (value) {
      try {
        const responseTrays = await axios.get(`/search/trays?name=${value}`);
        const responseCourses = await axios.get(`/search/courses?name=${value}`);
        const responseIngredients = await axios.get(`/search/ingredients?name=${value}`);
        const options = [];
        responseTrays.data.map((tray) => {
          options.push({
            label: tray.name,
            key: tray.id,
            type: "trays"
          });
        });
        responseCourses.data.map((course) => {
          options.push({
            label: course.name,
            key: course.id,
            type: "courses"
          });
        });
        responseIngredients.data.map((ingredient) => {
          options.push({
            label: ingredient.name,
            key: ingredient.id,
            type: "ingredients"
          });
        });
        setOptions(options);
      } catch (error) {
        console.log(error);
      }
    }
  };

  const onSearchClick = (e) => {
    window.location.replace(`/producto/${e.key}/${e.type}`);
  }

  return (
    <ul className={style.links}>
      <Link style={NavStyle} to="/">
        <li>Bandejas</li>
      </Link>
      <Link style={NavStyle} to="/platos">
        <li>Platos</li>
      </Link>
      <Link style={NavStyle} to="/ingredientes">
        <li>Ingredientes</li>
      </Link>
      <div>
          <Select
            isClearable={true}
            styles={customStyles} 
            isMulti={false}
            components={{ DropdownIndicator: null }}
            onChange={(value) => onSearchClick(value)}
            options={options}
            inputValue={searchName}
            onInputChange={(value) => updateSearchInput(value)}
            placeholder="Buscar..."
          />
      </div>
    </ul>
  );
}
