<script module>
  export function executeCommand(command) {
    switch (command.name) {
      case "forward":
        forward(command.value);
      case "backward":
        left(180);
        forward(command.value);
        left(180);
      case "left":
        left(command.value);
      case "right":
        right(command.value);
      case "penup":
        penup();
      case "pendown":
        pendown();
    }
  }
</script>

<div
  class="right-container d-flex flex-col m-3 align-items-center justify-content-center"
>
  <canvas id="turtlecanvas" width="600" height="600"></canvas>
  <canvas id="imagecanvas" width="600" height="600" style="display: none;"
  ></canvas>
  <script src="/lib/turtle.js" type="text/javascript"></script>
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
