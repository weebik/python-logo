<script module>
  import { io } from "socket.io-client";
  import { toastSuccess, toastError } from "./Toast.svelte";
  import { executeTurtleCommand } from "./Turtle.svelte";
  import { setRunningState } from "./ButtonBar.svelte";

  const socket = io();

  let connected = false;

  /**
   * Sends server the code to run
   */
  export function emitRun(code) {
    socket.emit("run", code);
  }

  /**
   * Sends server a stop signal
   */
  export function emitStop() {
    socket.emit("stop");
  }

  /**
   * Socket event listeners
   */
  socket.on("connect", () => {
    if (!connected) {
      console.log("Connected to the server.");
      connected = true;
    } else {
      console.log("Reconnected to the server.");
      toastSuccess("Reconnected to the server.");
    }
  });

  /**
   * Handle connection error
   */
  socket.on("connect_error", () => {
    toastError("Cannot connect to the server.");
  });

  /**
   * Handle connection closed
   */
  socket.on("disconnect", () => {
    console.error("Server connection closed.");
    toastError("Server connection closed.");
  });

  /**
   * Handle task status
   */
  socket.on("task", (data) => {
    if (data.status === "running") {
      setRunningState(true);
    } else if (data.status === "done") {
      setRunningState(false);
    } else if (data.status === "failed") {
      setRunningState(false);
      toastError(data.message);
      console.log("Error: ", data.message);
    }
  });

  /**
   * Handle turtle commands
   */
  socket.on("execute", (command) => {
    executeTurtleCommand(command);
  });
</script>
