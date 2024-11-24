<script module>
  export function resetTurtle() {
    reset();
  }
  export function executeCommand(command) {
    switch (command.name) {
      case "forward":
        forward(command.value);
        break;
      case "backward":
        left(180);
        forward(command.value);
        left(180);
        break;
      case "left":
        left(command.value);
        break;
      case "right":
        right(command.value);
        break;
      case "penup":
        penup();
        break;
      case "pendown":
        pendown();
        break;
    }
  }
</script>

<div
  class="right-container d-flex flex-col align-items-center justify-content-center p-5"
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
    max-height: calc(90vh - 140px);
    max-width: calc(90vh - 140px);
    background-color: #cae5be;
    border-radius: 10px;
    z-index: 0;
  }
</style>
