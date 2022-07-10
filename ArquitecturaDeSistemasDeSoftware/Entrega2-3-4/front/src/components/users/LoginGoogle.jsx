import React from "react";
import GoogleLogin from "react-google-login";
import useAuth from "../../hooks/useAuth";
import { connectWebSocket } from './Messager';

export const LoginGoogle = ({setSuccess}) => {

  const { setAuth } = useAuth();
  async function handleGoogleResponse (googleBody) {
    
      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ googleToken: googleBody.tokenId }),
      };
    
      const response = await fetch(
        `${process.env.REACT_APP_URL_BACK}/session/googleLogin`,
        requestOptions
      );
      if (!response.ok) {
        const error = await response.text();
        throw new Error(error);
      }
      setSuccess(true);
      const accessToken = await response.text();
      const pars = JSON.parse(accessToken);
      const token = pars.token;
      const user = "user";
      const pwd = "secret";

      connectWebSocket(token);

      setAuth({ user, pwd, token });
    };

  return (
    <GoogleLogin
      clientId={process.env.REACT_APP_GOOGLE_CLIENT_ID}
      buttonText="Iniciar Sesión con Google"
      onSuccess={handleGoogleResponse}
      onFailure={handleGoogleResponse}
      cookiePolicy={"single_host_origin"}
    />
  );
};
