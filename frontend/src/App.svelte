<script lang="js">
  import { SvelteToast } from "@zerodevx/svelte-toast";
  import ResizableContainer from "./components/ResizableContainer.svelte";
  import Header from "./components/Header.svelte";
  import ButtonBar from "./components/ButtonBar.svelte";
  import Textarea from "./components/Textarea.svelte";
  import Turtle from "./components/Turtle.svelte";
  import InfoBar from "./components/InfoBar.svelte";
  import Socket from "./components/Socket.svelte";
</script>

<main>
  <Header />
  <div
    class="container-fluid p-0 overflow-hidden d-flex flex-column"
    style="height: calc(100vh - 80px);"
  >
    <div class="row flex-grow-1">
      <div class="d-flex justify-content-center align-items-streach">
        <ResizableContainer>
          <ButtonBar />
          <Textarea />
        </ResizableContainer>
        <div
          class="right-container w-100 d-flex flex-column align-items-center justify-content-center overflow-hidden"
        >
          <Turtle />
          <InfoBar />
        </div>
      </div>
    </div>
  </div>
  <div class="toast-overrides">
    <SvelteToast />
  </div>
  <Socket />
</main>

<style>
  :global(body) {
    background-color: #0a273b;
  }
  .right-container {
    min-width: 550px;
    flex: 1;
  }
  .toast-overrides {
    --toastWidth: 24rem;
    --toastBackground: #ff3931;
    --toastColor: white;
    --toastBorderRadius: 1rem;
    --toastBarBackground: darkRed;
    --toastPadding: 0.75rem;
    font-family: Ubuntu, sans-serif;
  }
</style>
