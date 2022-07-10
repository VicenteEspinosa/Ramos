import { w3cwebsocket as W3CWebSocket } from "websocket";

const connectWebSocket = async (token, callback_f) => {
  console.log(process.env.REACT_APP_MESSAGING_WS);
  const client = await new W3CWebSocket(`ws://${process.env.REACT_APP_MESSAGING_WS}/chat`);

  client.onopen = () => {
    console.log("WebSocket Client Connected");
    sendJSONMessage(client, {
      type: "token",
      content: token,
    });
  };
  client.onmessage = (msg) => {
    console.log(msg);
    console.log("Receiving Message from WebSocket Client:");
    callback_f(msg);
    return msg
  };
  return client;
};

const sendJSONMessage = async (client, msg) => {
  console.log("Sending Message to WebSocket Client:");
  console.log(msg);
  await client.send(JSON.stringify(msg));
  console.log("Message Sent");
};

const createChatRoom = async (token) => {
  try {
    const requestOptions = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({
        name: "Chat por Ping",
        level_admin: 999,
        type: "user2user",
      }),
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
    console.log("Chat Room Created:");
    console.log({ data });
    return data;
  } catch (error) {
    console.log(error);
  }
};

const inviteUserToRoom = async (token, userUUID, room_id) => {
  try {
    const requestOptions = {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({
        entity_UUID: userUUID,
        permissions: "rw",
        level: "999",
      }),
    };

    const response = await fetch(
      `http://${process.env.REACT_APP_MESSAGING_WS}/rooms/${room_id}/members`,
      requestOptions
    );

    if (!response.ok) {
      const error = await response.text();
      throw new Error(error);
    }

    const rawData = await response.text();
    const data = JSON.parse(rawData);
    console.log("User Invited to Chat Room:");
    console.log({ data });
    return data;
  } catch (error) {
    console.log(error);
  }
};

export { connectWebSocket, sendJSONMessage, createChatRoom, inviteUserToRoom};
