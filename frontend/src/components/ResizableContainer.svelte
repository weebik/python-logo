<script lang="js">
  import { onMount } from "svelte";
  let resizable;
  let resizer;

  function initResize() {
    window.addEventListener("mousemove", startResizing);
    window.addEventListener("mouseup", stopResizing);
  }

  function startResizing(e) {
    resizable.style.width = e.clientX - resizable.offsetLeft + "px";
  }

  function stopResizing() {
    window.removeEventListener("mousemove", startResizing);
    window.removeEventListener("mouseup", stopResizing);
  }

  onMount(() => {
    resizer.addEventListener("mousedown", initResize);
    return () => {
      resizer.removeEventListener("mousedown", initResize);
    };
  });
</script>

<div bind:this={resizable} class="left-container d-flex">
  <div bind:this={resizer} class="resizer"></div>
  <slot></slot>
</div>

<style>
  .left-container {
    min-width: 500px;
    position: relative;
    width: 50%;
    flex-direction: column;
    padding-right: 10px;
  }
  .resizer {
    width: 10px;
    height: 100%;
    background: #153246;
    position: absolute;
    right: 0;
    bottom: 0;
    cursor: col-resize;
    z-index: 1;
  }
</style>
