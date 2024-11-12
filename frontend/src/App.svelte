<script lang="js">
  import ResizableContainer from "./components/ResizableContainer.svelte";
  import Header from "./components/Header.svelte";
  import ButtonBar from "./components/ButtonBar.svelte";
  import Textarea from "./components/Textarea.svelte";
  import CanvasArea from "./components/CanvasArea.svelte";
  import logo from "./assets/logo.png";

  let code = "";

  async function sendCode() {
    const textarea = document.getElementById("codeTextarea");
    if (textarea && textarea instanceof HTMLTextAreaElement) {
      const code = textarea.value;
      fetch("/", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: new URLSearchParams({ code: code }),
      })
        .then((response) => {
          if (response.redirected) {
            window.location.href = response.url;
          }
        })
        .catch((error) => console.error("Error:", error));
    }
  }
</script>

<main>
  <Header {logo} />
  <div class="container">
    <ResizableContainer>
      <ButtonBar on:run={sendCode} />
      <Textarea id="codeTextarea" bind:value={code} />
    </ResizableContainer>
    <CanvasArea />
  </div>
</main>

<style>
  .container {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    width: 100%;
    height: calc(100vh - 100px);
    margin: 0;
  }
</style>
