<script module>
  import { io } from "socket.io-client";
  import { executeCommand } from "./Turtle.svelte";

  const socket = io();

  export function emit(event, data) {
    socket.emit(event, data);
  }

  socket.on("connect", () => {
    console.log("Connected to server");
  });

  socket.on("execute", (command) => {
    console.log("Executing command:", command);
    executeCommand(command);
  });
</script>
