import { useEffect, useState } from "react";
import useAuth from "../../hooks/useAuth";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faSun, faCloudRain } from '@fortawesome/free-solid-svg-icons'
import { Button, Icon } from "react-bulma-components";
import { createChatRoom, inviteUserToRoom } from "./Messager";

const getUserByID = async (token, userID) => {
  try {
    const requestOptions = {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
    };

    const response = await fetch(
      `${process.env.REACT_APP_URL_BACK}/users/${userID}`,
      requestOptions
    );

    if (!response.ok) {
      const error = await response.text();
      throw new Error(error);
    }

    const rawData = await response.text();
    const data = JSON.parse(rawData);
    console.log(data);
    console.log(data.userUUID);
    return data.userUUID;
  } catch (error) {
    console.log(error);
  }
};

const Profile = () => {
  const { auth } = useAuth();
  const [userData, setUserData] = useState();
  const [locations, setLocations] = useState([]);
  const [receivedUser, setReceivedUser] = useState([]);
  const [myPings, setMyPings] = useState([]);
  const [api, setApi] = useState([]);

  const approvePing = async (pingID, senderID) => {
    putPingData(pingID, true);

    const newRoom = createChatRoom(auth.token);
    newRoom.then(async (response) => {
      const userToInvite = await getUserByID(auth.token, senderID);
      console.log(userToInvite);

      inviteUserToRoom(auth.token, userToInvite, response.content.room.id);
    });
  };

  const rejectPing = async (pingID) => {
    putPingData(pingID, false);
  };

  const putPingData = async (pingID, state) => {
    try {
      const requestOptions = {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json', 'token': auth.token },
        body : JSON.stringify({
          'approved': state
        })
      };
      const response = await fetch(`${process.env.REACT_APP_URL_BACK}/pings/${pingID}`, requestOptions);
      if (!response.ok) {
        const error = await response.text();
        throw new Error(error);
      }
      window.location.reload(false);
    } catch (error) {
      console.log(error);
    }
  }

  useEffect(() => {
    const getUserData = async () => {
      try {
        const requestOptions = {
          method: 'GET',
          headers: { 'Content-Type': 'application/json', 'token': auth.token }
        };
        const response = await fetch(`${process.env.REACT_APP_URL_BACK}/users/profile`, requestOptions);
        if (!response.ok) {
          const error = await response.text();
          throw new Error(error);
        }

        console.log(response);
        const rawData = await response.text();
        const data = JSON.parse(rawData);
        setUserData(data);

        data.locations.map(locationID => addLocationByID(locationID));
        data.pings.received.map(pingID => addPingById(pingID));
        data.pings.sent.map(pingId => addPingById(pingId));
      } catch (error) {
        console.log(error);
      }
    }

    const addLocationByID = async locationID => {
      try {
        const requestOptions = {
          method: 'GET',
          headers: { 'Content-Type': 'application/json', 'token': auth.token }
        };
        const response = await fetch(`${process.env.REACT_APP_URL_BACK}/locations/${locationID}`, requestOptions);
        if (!response.ok) {
          const error = await response.text();
          throw new Error(error);
        }

        const rawData = await response.text();
        const data = JSON.parse(rawData);
        // NOTA: La siguiente linea produce resultados duplicados al utilizar StrictMode.
        // Es porque agrega cosas al arreglo cada vez que se renderiza el componente, entonces el arreglo
        // solo se reinicia cada vez que llega al end point por primera vez.
        setLocations(oldData => [...oldData, data]);
      } catch (error) {
        console.log(error);
      }
      return null;
    }

    const addPingById = async pingID => {
      try {
        const requestOptions = {
          method: 'GET',
          headers: { 'Content-Type': 'application/json', 'token': auth.token }
        };
        const response = await fetch(`${process.env.REACT_APP_URL_BACK}/pings/${pingID}`, requestOptions);
        if (!response.ok) {
          const error = await response.text();
          throw new Error(error);
        }

        const rawData = await response.text();
        const data = JSON.parse(rawData);
        // NOTA: La siguiente linea produce resultados duplicados al utilizar StrictMode.
        // Es porque agrega cosas al arreglo cada vez que se renderiza el componente, entonces el arreglo
        // solo se reinicia cada vez que llega al end point por primera vez.
        AddUserById(data.from);
        setMyPings(oldData => [...oldData, data]);
      } catch (error) {
        console.log(error);
      }
      return null;
    }

    const getAPI = async () => {
      try {
        const requestOptions = {
          method: 'GET',
          headers: { 'Content-Type': 'application/json', 'token': auth.token }
        };
        const response = await fetch(`${process.env.REACT_APP_URL_BACK}/locations/api/weather`, requestOptions);
        if (!response.ok) {
          const error = await response.text();
          throw new Error(error);
        }

        const data = await response.json();
        setApi(data);
      } catch (error) {
        console.log(error);
      }
      return null;
    }

    const AddUserById = async id => {
      try {
        const requestOptions = {
          method: 'GET',
          headers: { 'Content-Type': 'application/json', 'token': auth.token }
        };
        const response = await fetch(`${process.env.REACT_APP_URL_BACK}/users/${id}`, requestOptions);
        if (!response.ok) {
          const error = await response.text();
          throw new Error(error);
        }

        const rawData = await response.text();
        const data = JSON.parse(rawData);
        setReceivedUser(oldData => [...oldData, data.username]);
      } catch (error) {
        console.log(error);
      }
      return null;
    }

    getUserData();
    getAPI();
  }, [auth.token]);

  return (
    <>
      {
        userData ? (
          <article className="margins">
            <div className="columns">
              <div className="column">
                <h1 className="title">User Profile</h1>
                <h2 className="subtitle is-5">Username: {userData.username}</h2>
                <h2 className="subtitle is-5">Email: {userData.email}</h2>
                <br />
                <h2 className="subtitle is-4">My locations:</h2>
                {
                  locations?.length ? (
                    <>
                      <ul>
                        {
                          locations.map((location, i) =>
                            <li key={i} className="subtitle is-5">
                              "{location?.name}": ({location?.location.coordinates[0]}, {location?.location.coordinates[1]})
                              {api[0] ? (
                                <Icon size="large">
                                  <FontAwesomeIcon icon={faSun} />
                                </Icon>
                              ) : (
                                <Icon size="large">
                                  <FontAwesomeIcon icon={faCloudRain} />
                                </Icon>
                              )}
                            </li>)
                        }
                      </ul>
                      <br />
                      <Button.Group>
                        <a href="/locations">
                          <Button rounded color="primary">Agrega ubicaciones</Button>
                        </a>
                      </Button.Group>
                    </>
                  ) : <p>Aún no tienes ubicaciones... <a href="/locations">¡Agrega aquí!</a></p>
                }
              </div>
              <div className="column is-fixed-top">
                <h2 className="subtitle is-4">Solicitudes pendientes:</h2>
                  {
                    <>
                      <ul>
                        {
                          myPings.map((ping, i) => {
                            if (ping.state === "pending" && ping.to === userData._id) {
                              return (
                              <li key={i} className="subtitle is-5">
                                <div className="columns is-vcentered">
                                  <div className="column is-8">
                                    From: {receivedUser[i]}
                                    <p></p>
                                    State: {ping.state}
                                  </div>
                                  <div className="column">
                                    <Button color="primary" onClick={() => approvePing(ping._id, ping.from)}>Aceptar</Button>
                                    <Button color="danger" onClick={() => rejectPing(ping._id)}>Rechazar</Button>
                                  </div>
                                </div>
                              </li>
                              )
                            }
                            return null;
                          })
                        }
                      </ul>
                      <br />
                    </>
                  }
                <h2 className="subtitle is-4">Mis Pings (y datos dindin):</h2>
                {myPings.map((ping, id) => {
                    if (ping.state === "approved") {
                        return (
                            <li key={id} className="subtitle is-5">
                                <div className="columns is-vcentered">
                                    <div className="column is-8">
                                        Enviado por: {receivedUser[id]}
                                        <p></p>
                                        Recibido por: {userData.username}
                                        <p></p>
                                        Distancia: {ping.distance.$numberDecimal}
                                        <p></p>
                                        Dindin 😏:{parseFloat(ping.dindin.$numberDecimal)}
                                    </div>
                                </div>
                            </li>
                        )
                    } return null;
                })}
              </div>
            </div>
          </article>
        ) : null
      }
    </>
  );
};

export default Profile;