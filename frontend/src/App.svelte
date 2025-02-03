<script lang="js">
  import ButtonBar from "./components/ButtonBar.svelte";
  import Header from "./components/Header.svelte";
  import InfoBar from "./components/InfoBar.svelte";
  import ResizableHorizontal from "./components/ResizableHorizontal.svelte";
  import Socket from "./components/Socket.svelte";
  import Textarea from "./components/Textarea.svelte";
  import Toast from "./components/Toast.svelte";
  import Turtle from "./components/Turtle.svelte";
  import themeColor from "./storeThemes.js";
</script>

<main class={$themeColor}>
  <Header />
  <div
    class="container-fluid p-0 overflow-hidden d-flex flex-column"
    style="height: calc(100vh - 80px);"
  >
    <div class="row flex-grow-1">
      <div class="d-flex justify-content-center align-items-streach">
        <ResizableHorizontal>
          <ButtonBar />
          <Textarea />
        </ResizableHorizontal>
        <div
          class="right-container w-100 d-flex flex-column align-items-center justify-content-center overflow-hidden"
        >
          <Turtle />
          <InfoBar />
        </div>
      </div>
    </div>
  </div>
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
    &.dark {
      background-color: var(--bg-dark);
    }
    &.light {
      background-color: var(--bg-light);
    }
  }

  .right-container {
    min-width: 550px;
    flex: 1;
  }
</style>
