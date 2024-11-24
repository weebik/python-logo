<div>
  <div class="button-bar d-flex align-items-center justify-content-around">
    <div class="d-flex space-around p-0 gap-2">
      <button class="p-0 m-0" title="Run code">
        <img src="/run.svg" alt="Run" />
      </button>
      <button class="p-0 m-0" title="Run command">
        <img src="/run-debug.svg" alt="Run debug" />
      </button>
      <button class="p-0 m-0" title="Pause">
        <img src="/pause.svg" alt="Pause" />
      </button>
      <button class="p-0 m-0" title="Stop">
        <img src="/stop.svg" alt="Stop" />
      </button>
    </div>
    <div class="d-flex p-0 gap-2">
      <button class="p-0 m-0" title="Import code">
        <img src="/import-code.svg" alt="Import" />
      </button>
      <button class="p-0 m-0" title="Export code">
        <img src="/export-code.svg" alt="Export" />
      </button>
    </div>
  </div>
</div>

<style>
  .button-bar {
    background-image: url("/button-bar.svg");
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
