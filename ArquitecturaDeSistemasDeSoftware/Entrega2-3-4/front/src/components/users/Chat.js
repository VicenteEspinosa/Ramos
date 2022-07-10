import { useEffect, useRef, useState } from 'react';
import useAuth from '../../hooks/useAuth';
import { Link, useParams } from 'react-router-dom';
import { sendJSONMessage, recieveMsg, connectWebSocket } from './Messager';

// Bulma and Icons
import { Button, Form, Icon } from "react-bulma-components";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faUser, faLock, faCircleCheck } from '@fortawesome/free-solid-svg-icons'
import { LoginGoogle } from "./LoginGoogle";

const Chat = ({ client, setClient }) => {
    const id = useParams();
    const msgRef = useRef();
    const [history, setHistory] = useState([]);
    const [received, setReceived] = useState([]);
    const [msg, setMsg] = useState('');
    const [errMsg, setErrMsg] = useState('');
    const {auth} = useAuth();

    const newMessage = async (msg) => {
        const parsed = JSON.parse(msg.data)
        if (parsed.type === "message"){
            setReceived(oldData => [...oldData, parsed.data]);
            
        }
    }
    // conect to room
    const ConnectToRoom = async () => {
        function sleep(ms) {
            return new Promise(resolve => setTimeout(resolve, ms));
        };
        await sleep(2000);
        try {
            const message = {
                room_id: parseInt(id.id),
                type: "select_room"
            }
            await sendJSONMessage(client, message);
        } catch (error) {
            console.log(error)
            setErrMsg(error.message);
        }
    }
    // función que se activa al apretar botón enviar

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const message = {
                content: msg,
                type: "message"
            }
            sendJSONMessage(client, message);
        }catch (error) {
            console.log(error)
            setErrMsg(error.message);
        }
        setMsg("");
    }

    useEffect(() => {
        const ws = async () => {
            if (auth.token) {
              const newClient = await connectWebSocket(auth.token, newMessage)
              setClient(newClient);
            }
        }
        ws();
      }, [auth.token]);

    useEffect(() => {
        // función que carga historial del chat
        const loadHistory = async () => {
            try {
              const requestOptions = {
                method: "GET",
                headers: {
                  "Content-Type": "application/json",
                  Authorization: `Bearer ${auth.token}`,
                },
              };
        
              const response = await fetch(
                `http://${process.env.REACT_APP_MESSAGING_WS}/rooms/${id.id}/messages`,
                requestOptions
              );
        
              if (!response.ok) {
                const error = await response.text();
                throw new Error(error);
              }
        
              const rawData = await response.text();
              const data = JSON.parse(rawData);
              setHistory(data.content);
              console.log(data.content);
            } catch (error) {
              console.log(error);
            }
            console.log(history);
            // setHistory(response);
            return null;
        };
        
        // función que se activa al recibir mensaje
        loadHistory();
        ConnectToRoom();
        //sleep 1 second
        
    }
    , [client]);
    return (
        <>
        {
            history.map(message => (
            <div key={message.content} className="message">
                <span>{message.emitter} : {message.content}</span>
             </div>
            ))
        }
        {
            received.map((message,i) => (
            <div key={message.content} className="message">
                <span>{message.emitter} :{message.content}</span>
             </div>
            ))
        }
        <section className="margins">
        <Form.Field>
            <Form.Label htmlFor="username">Mensaje</Form.Label>
            <Form.Control>
                <Form.Input
                    type="text"
                    id="username"
                    href={msgRef}
                    autoComplete="off"
                    onChange={(e) => setMsg(e.target.value)}
                    value={msg}
                    required
                    placeholder="Username"
                />
            </Form.Control>
        </Form.Field>
        <Button.Group>
                <Button fullwidth rounded color="primary" onClick={handleSubmit} >Enviar</Button>
        </Button.Group>
        </section>
        </>
    )
};

export default Chat;