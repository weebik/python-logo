<script>
  import { onMount } from "svelte";

  onMount(() => {
    const script = document.createElement("script");
    script.src = "https://rawgit.com/hanumanum/js-turtle/master/lib/library.js";
    script.type = "text/javascript";
    script.async = true;

    script.onload = () => {
      console.log("Turtle loaded successfully.");
    };

    document.head.appendChild(script);

    return () => {
      document.head.removeChild(script);
    };
  });
</script>

<div class="right-container">
  <canvas id="turtlecanvas" width="700" height="700"></canvas>
  <canvas id="imagecanvas" width="700" height="700" style="display: none;"
  ></canvas>
</div>

<style>
  .right-container {
    display: flex;
    align-items: center;
    justify-content: center;
    flex: 1;
    min-width: 400px;
    width: 100%;
    height: 100%;
    overflow: hidden;
  }
  canvas {
    width: 100%;
    height: auto;
    border: 1px solid black; /* for debugging */
    z-index: 0;
  }
</style>
