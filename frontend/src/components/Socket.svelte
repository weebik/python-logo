<script module>
  import { io } from "socket.io-client";
  import { executeTurtleCommand } from "./Turtle.svelte";

  const socket = io();

  export function emitRun(code) {
    socket.emit("run", code);
  }

  socket.on("connect", () => {
    console.log("Connected to server");
  });

  socket.on("execute", (command) => {
    console.log("Received execute:", command);
    executeTurtleCommand(command);
  });
</script>
