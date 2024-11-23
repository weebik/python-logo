<script lang="js">
  import { createEventDispatcher } from "svelte";
  import bootstrap from "bootstrap/dist/js/bootstrap.bundle.min.js";

  const dispatch = createEventDispatcher();

  function handleRunClick() {
    dispatch("run");
    console.log("Run button clicked");
  }
  function handleRunCommandClick() {
    dispatch("run");
  }
  function handlePauseClick() {
    dispatch("run");
  }
  function handleStopClick() {
    dispatch("run");
  }
  function handleImportClick() {
    dispatch("run");
  }
  function handleExportClick() {
    dispatch("run");
  }

  var tooltipTriggerList = [].slice.call(
    document.querySelectorAll('[data-bs-toggle="tooltip"]')
  );
  var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
  });
</script>

<div>
  <div
    class="d-flex align-items-center justify-content-around"
    style="background-image: url('/buttonBar.svg'); height: 60px; z-index: 1;"
  >
    <div class="d-flex space-around p-0 gap-2">
      <button
        class="p-0 m-0"
        on:click={handleRunClick}
        data-bs-toggle="tooltip"
        data-bs-placement="bottom"
        title="Run code"
      >
        <img src="/play.svg" alt="Run" />
      </button>
      <button class="p-0 m-0">
        <img
          src="/runCommand.svg"
          alt="Run command"
          data-bs-toggle="tooltip"
          data-bs-placement="bottom"
          title="Run command"
        />
      </button>
      <button class="p-0 m-0">
        <img
          src="/pause.svg"
          alt="Pause"
          data-bs-toggle="tooltip"
          data-bs-placement="bottom"
          title="Pause"
        />
      </button>
      <button class="p-0 m-0">
        <img
          src="/stop.svg"
          alt="Stop"
          data-bs-toggle="tooltip"
          data-bs-placement="bottom"
          title="Stop"
        />
      </button>
    </div>
    <div class="d-flex p-0 gap-2">
      <button class="p-0 m-0">
        <img
          src="/importCode.svg"
          alt="Import"
          data-bs-toggle="tooltip"
          data-bs-placement="bottom"
          title="Import code"
        />
      </button>
      <button class="p-0 m-0">
        <img
          src="/exportCode.svg"
          alt="Export"
          data-bs-toggle="tooltip"
          data-bs-placement="bottom"
          title="Export code"
        />
      </button>
    </div>
  </div>
</div>

<style>
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
