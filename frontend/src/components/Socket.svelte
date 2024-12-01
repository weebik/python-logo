<script module>
  import { io } from "socket.io-client";
  import { toastSuccess, toastError } from "./Toast.svelte";
  import { executeTurtleCommand } from "./Turtle.svelte";

  const socket = io();

  let connected = false;

  export function emitRun(code) {
    socket.emit("run", code);
  }

  socket.on("connect", () => {
    if (!connected) {
      console.log("Connected to the server.");
      connected = true;
    } else {
      console.log("Reconnected to the server.");
      toastSuccess("Reconnected to the server.");
    }
  });

  socket.on("connect_error", () => {
    toastError("Cannot connect to the server.");
  });

  socket.on("disconnect", () => {
    console.error("Server connection closed.");
    toastError("Server connection closed.");
  });

  socket.on("execute", (command) => {
    console.log("Received execute: ", command);
    executeTurtleCommand(command);
  });

  socket.on("exception", (message) => {
    console.log("Error: ", message);
    toastError(message);
  });
</script>
