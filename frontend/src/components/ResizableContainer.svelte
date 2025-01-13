<script lang="js">
  import themeColor from "../storeThemes.js";

  let { children } = $props();

  let resizable;

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
</script>

<div bind:this={resizable} class="left-container d-flex">
  <div
    role="button"
    tabindex="0"
    onmousedown={initResize}
    class="resizer {$themeColor}"
  ></div>
  {@render children()}
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
    position: absolute;
    right: 0;
    bottom: 0;
    cursor: col-resize;
    z-index: 1;
    &.light {
      background: var(--ter-pri-light);
    }
    &.dark {
      background: var(--ter-pri-dark);
    }
  }
</style>
