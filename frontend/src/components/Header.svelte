<script>
  import themeColor, { storeThemes } from "../storeThemes.js";
  import logo from "../assets/logo.png";
  import Icon from "./Icon.svelte";

  function ThemeToggler(e) {
    if ($themeColor === "dark") {
      storeThemes.update((themeColor) => "light");
    } else {
      storeThemes.update((themeColor) => "dark");
    }
  }
</script>

<header
  class="header d-flex w-100 justify-content-center align-items-center user-select-none"
>
  <div class="d-flex justify-content-center align-items-center flex-grow-1">
    <img
      class="m-1 user-select-none"
      alt="Logo"
      src={logo}
      style="width: 60px; height: 60px;"
    />
    <h1 style="font-weight: bold; margin: 5px;">Logo Playground</h1>
  </div>
  <button class="theme-button ms-auto me-3" onclick={ThemeToggler}>
    {#if $themeColor === "dark"}
      <Icon name="light" />
    {:else}
      <Icon name="dark" />
    {/if}
  </button>
</header>

<style>
  .header {
    background: linear-gradient(90deg, var(--pri1) 20%, var(--pri2) 100%);
    color: white;
    height: 80px;
    z-index: 10;
  }
  .theme-button {
    background-color: transparent;
    border: none;
    cursor: pointer;
    color: var(--acc1);
    transition:
      scale 0.2s,
      color 0.05s;
    &:hover {
      color: var(--acc2);
    }
    &:enabled:hover {
      scale: 1.1;
      color: var(--acc2);
    }
    &:enabled:active {
      scale: 1.05;
      color: var(--acc2);
    }
  }
</style>
