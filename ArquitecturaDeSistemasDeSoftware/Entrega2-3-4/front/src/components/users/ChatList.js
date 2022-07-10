import { useEffect, useRef, useState } from "react";
import useAuth from "../../hooks/useAuth";
import { Link, useParams } from "react-router-dom";
import { sendJSONMessage, recieveMsg, connectWebSocket } from "./Messager";

// Bulma and Icons
import { Button, Form, Icon } from "react-bulma-components";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faUser,
  faLock,
  faCircleCheck,
} from "@fortawesome/free-solid-svg-icons";
import { LoginGoogle } from "./LoginGoogle";

const ChatList = () => {
  const [chats, setChats] = useState([]);
  const { auth } = useAuth();

  useEffect(() => {
    const loadChats = async () => {
      try {
        const requestOptions = {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${auth.token}`,
          },
        };

        const response = await fetch(
          `http://${process.env.REACT_APP_MESSAGING_WS}/rooms`,
          requestOptions
        );

        if (!response.ok) {
          const error = await response.text();
          throw new Error(error);
        }

        const rawData = await response.text();
        const data = JSON.parse(rawData);
        console.log(data);
        setChats(data.content);
      } catch (error) {
        console.log(error);
      }
      return null;
    };
    loadChats();
  }, []);

  return (
    <>
      {chats.map((room, i) => (
        <div key={room.room_id} className="message">
            <a href={`/chat/${room.room_id}`} >Sala {room.room_id}</a>
        </div>
      ))}
    </>
  );
};

export default ChatList;
