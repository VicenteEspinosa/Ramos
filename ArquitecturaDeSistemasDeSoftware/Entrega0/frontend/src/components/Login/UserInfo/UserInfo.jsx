import style from "./userInfo.module.css";
import {getUser} from "../../../utils";

const UserInfo = ({updateLogin}) => {
  const destroyToken = (e) => {
    e.preventDefault();
    document.cookie = "token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    updateLogin(false);
  };
  if (getUser() === undefined || getUser() === null) {
    destroyToken();
    updateLogin(false);
  };
  return (
    <div className={style.general}>
      <h2 className={style.title}>
        Bienvenid@
        {" " + getUser().username}
      </h2>
      <div className={style.logout}>
        <div className={style.buttonHolder}>
          <button
            onClick={destroyToken}
            className={style.sesionButton}
            type="submit"
          >
            Cerrar Sesion
          </button>
        </div>
      </div>
    </div>
  );
};

export default UserInfo;
