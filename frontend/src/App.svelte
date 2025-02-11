<script lang="js">
  import Header from "./components/Header.svelte";
  import Socket from "./components/Socket.svelte";
  import Toast from "./components/Toast.svelte";
  import themeColor from "./storeThemes.js";
  import MainLayout from "./components/MainLayout.svelte";
</script>

<main class={$themeColor}>
  <Header />
  <MainLayout />
  <Toast />
  <Socket />
</main>

<style>
  :global(*) {
    font-family: "Ubuntu", sans-serif;
  }
  :global(:root) {
    --pri1: #70f1c9;
    --pri2: #26b1b7;
    --sec: #309f7f;
    --acc1: #cae5be;
    --acc2: #92da8c;
    /* light mode*/
    --bg-light: #cae5be;
    --ter-pri-light: #add6a9;
    --ter-sec-light: #309f8090;
    --text-light: #154644;
    --placeholder-light: #627d90;
    --canvas-light: #add6a9;
    /* dark mode */
    --bg-dark: #0a273b;
    --ter-pri-dark: #153246;
    --ter-sec-dark: #0f2534;
    --text-dark: #cae5be;
    --placeholder-dark: #627d90;
    --canvas-dark: #153246;
  }

  main {
    height: 100vh;
    &.dark {
      background-color: var(--bg-dark);
    }
    &.light {
      background-color: var(--bg-light);
    }
  }
</style>
