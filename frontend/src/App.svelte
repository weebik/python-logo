<script lang="js">
  import ResizableContainer from "./components/ResizableContainer.svelte";
  import Header from "./components/Header.svelte";
  import ButtonBar from "./components/ButtonBar.svelte";
  import Textarea from "./components/Textarea.svelte";
  import CanvasArea from "./components/CanvasArea.svelte";
  import InfoBar from "./components/InfoBar.svelte";
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
          <Textarea id="codeTextarea" />
        </ResizableContainer>
        <div
          class="right-container w-100 d-flex flex-column align-items-center justify-content-center overflow-hidden"
        >
          <CanvasArea />
          <InfoBar />
        </div>
      </div>
    </div>
  </div>
</main>

<style>
  :global(body) {
    background-color: #0a273b;
  }
  .right-container {
    min-width: 550px;
    flex: 1;
  }
</style>
