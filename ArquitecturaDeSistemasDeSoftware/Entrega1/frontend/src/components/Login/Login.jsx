import React, { useState } from "react";
import style from "./login.module.css";
import axios from "axios";

const Login = ({ updateLogin }) => {
  const [query_username, updateUsername] = useState("");
  const [query_password, updatePassword] = useState("");
  const [query_contact, updateContact] = useState("");
  const [query_mail, updateMail] = useState("");
  const [registerMode, setRegisterMode] = useState(false);

  const [allData, updateAllData] = useState(true);
  const [correctData, updateCorrectData] = useState(true);
  const [takenUsername, updateTakenUsername] = useState(false);
  const [createdUser, updateCreatedUser] = useState(false);

  const sendPost = async (e) => {
    updateCreatedUser(false);
    e.preventDefault();
    updateTakenUsername(false);
    if (query_username === "" || query_password === "") {
      updateAllData(false);
      updateCorrectData(true);
      return;
    }
    if (registerMode) {
      if (query_contact === "" || query_mail === "") {
        updateCorrectData(true);
        updateAllData(false);
        return;
      }
      updateAllData(true);
      try {
        await axios.post("user/create", {
          username: query_username,
          password: query_password,
          contact: query_contact,
          mail: query_mail,
        });
        updateCreatedUser(true);
      } catch (error) {
        if (error.response.status === 401) {
          updateTakenUsername(true);
        }
      }
    } else {
      updateAllData(true);
      try {
        const data = await axios.post("user/login", {
          username: query_username,
          password: query_password,
        });
        document.cookie = `token=${data.data.token}`;
        updateLogin(true);
      } catch (err) {
        updateCorrectData(false);
      }
    }
  };

  const swapRegisterMode = (e) => {
    e.preventDefault();
    updateMail("");
    updateContact("");
    updatePassword("");
    updateUsername("");
    updateCorrectData(true);
    updateAllData(true);
    updateTakenUsername(false);
    updateCreatedUser(false);
    setRegisterMode(!registerMode);
  };

  return (
    <div className={style.general}>
      <div className={style.title}>{registerMode ? "Registro" : "Login"}</div>
      <div className={style.form}>
        <label className={style.label}>
          <p>Ususario</p>
          <input
            className={style.input}
            placeholder="Usuario"
            name="username"
            value={query_username}
            onChange={(e) => updateUsername(e.target.value)}
          ></input>
        </label>
        <label className={style.label}>
          <p>Contraseña</p>
          <input
            className={style.input}
            placeholder="Contraseña"
            name="password"
            value={query_password}
            onChange={(e) => updatePassword(e.target.value)}
          ></input>
        </label>
        {registerMode ? (
          <div className={style.form}>
            <label className={style.label}>
              <p>Contacto</p>
              <input
                className={style.input}
                placeholder="Contacto"
                name="contact"
                value={query_contact}
                onChange={(e) => updateContact(e.target.value)}
              ></input>
            </label>
            <label className={style.label}>
              <p>Mail</p>
              <input
                className={style.input}
                placeholder="Mail"
                name="mail"
                value={query_mail}
                onChange={(e) => updateMail(e.target.value)}
              ></input>
            </label>
          </div>
        ) : null}
        {allData ? null : (
          <div className={style.error}>Rellena todos los datos</div>
        )}
        {takenUsername ? (
          <div className={style.error}>Usuario ya registrado</div>
        ) : null}
        {correctData ? null : (
          <div className={style.error}>Usuario o contraseña incorrecto</div>
        )}
        {createdUser ? (
          <div className={style.success}>Usuario registrado</div>
        ) : null}
      </div>
      <div className={style.buttonHolder}>
        <button onClick={sendPost} className={style.postButton} type="submit">
          {registerMode ? "Registrarse" : "Iniciar sesion"}
        </button>
      </div>
      <div className={style.buttonHolder}>
        <button
          onClick={swapRegisterMode}
          className={style.swapButton}
          type="submit"
        >
          {registerMode ? "Ir a iniciar sesion" : "Ir a registrarse"}
        </button>
      </div>
    </div>
  );
};

export default Login;
