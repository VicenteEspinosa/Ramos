import { decodeToken } from "react-jwt";

const getCookie = (name) => {
  var nameEQ = name + "=";
  var ca = document.cookie.split(";");
  for (var i = 0; i < ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) === " ") c = c.substring(1, c.length);
    if (c.indexOf(nameEQ) === 0) {
      const cookie = c.substring(nameEQ.length, c.length);
      if (cookie !== undefined) return cookie;
    }
  }
  return null;
};

const getUser = () => {
  const token = getCookie("token");
  if (token) {
    const user = decodeToken(token);
    return user;
  }
  return null;
}


export {getUser, getCookie};
