<script>
  import Icon from "./Icon.svelte";
  import { code } from "./Textarea.svelte";
  import { runTurtle, resetTurtle } from "./Turtle.svelte";

  function handleRun() {
    runTurtle(code);
  }

  function handleReset() {
    resetTurtle();
  }
</script>

<div>
  <div class="button-bar d-flex align-items-center justify-content-around">
    <div class="d-flex space-around p-0 gap-2">
      <button class="p-0 m-0" title="Run code" onclick={handleRun}>
        <Icon name="run" />
      </button>
      <button class="p-0 m-0" title="Run command">
        <Icon name="runDebug" />
      </button>
      <button class="p-0 m-0" title="Pause">
        <Icon name="pause" />
      </button>
      <button class="p-0 m-0" title="Reset" onclick={handleReset}>
        <Icon name="reset" />
      </button>
    </div>
    <div class="d-flex p-0 gap-2">
      <button class="p-0 m-0" title="Import code">
        <Icon name="importCode" />
      </button>
      <button class="p-0 m-0" title="Export code">
        <Icon name="exportCode" />
      </button>
    </div>
  </div>
</div>

<style>
  .button-bar {
    background-image: url("/src/assets/button-bar.svg");
    height: 60px;
    z-index: 1;
  }
  button {
    user-select: none;
    border: none;
    background-color: transparent;
    transition:
      scale 0.2s,
      filter 0.05s;
    filter: invert(90%) sepia(3%) saturate(1480%) hue-rotate(53deg)
      brightness(113%) contrast(106%);
  }
  button:hover {
    scale: 1.1;
    filter: invert(90%) sepia(16%) saturate(674%) hue-rotate(62deg)
      brightness(103%) contrast(96%);
  }
  button:active {
    scale: 1.05;
    filter: invert(90%) sepia(16%) saturate(674%) hue-rotate(62deg)
      brightness(113%) contrast(96%);
  }
</style>
