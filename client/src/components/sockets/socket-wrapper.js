import React from "react";
import io from "socket.io-client";

const socket = io(process.env.BASE_URL + ":" + process.env.API_PORT);

function SocketWrapper(WrappedComponent) {
  return <WrappedComponent {...socket} />;
}

export default SocketWrapper;
