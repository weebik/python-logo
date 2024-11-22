<script>
  import { onMount } from "svelte";

  onMount(() => {
    const script = document.createElement("script");
    script.src = "/lib/turtle.js";
    script.type = "text/javascript";
    script.async = true;

    script.onload = () => {
      console.log("TurtleAPI loaded successfully.");
    };
    document.head.appendChild(script);
  });
</script>

<div
  class="right-container d-flex flex-col m-3 align-items-center justify-content-center"
>
  <canvas id="turtlecanvas" width="600" height="600"></canvas>
  <canvas id="imagecanvas" width="600" height="600" style="display: none;"
  ></canvas>
</div>

<style>
  .right-container {
    flex: 1;
    width: 100%;
  }
  canvas {
    width: 100%;
    max-height: calc(94vh - 140px);
    max-width: calc(94vh - 140px);
    background-color: #cae5be;
    border-radius: 10px;
    z-index: 0;
  }
</style>
