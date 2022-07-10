import style from "./searchUsers.module.css";
import { useState } from "react";

const SearchUsers = ({ setusersIds, updateShowMultipleMaps }) => {
  const [inputUsers, updateInputUsers] = useState("");
  const updateUsers = (e) => {
    e.preventDefault();
    updateShowMultipleMaps(true);
    setusersIds(inputUsers.replace(/\s/g, ""));
  };
  return (
    <div className={style.general}>
      <div className={style.search}>
        <input
          className={style.input}
          placeholder="IDs separados por coma"
          value={inputUsers}
          onChange={(e) => updateInputUsers(e.target.value)}
        ></input>
        <button
          onClick={updateUsers}
          className={style.button}
          type="submit"
        >
          Ver mapas
        </button>
      </div>
    </div>
  );
};

export default SearchUsers;
