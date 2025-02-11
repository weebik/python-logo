<script lang="js">
  import ButtonBar from "./components/ButtonBar.svelte";
  import Header from "./components/Header.svelte";
  import InfoBar from "./components/InfoBar.svelte";
  import Socket from "./components/Socket.svelte";
  import Textarea from "./components/Textarea.svelte";
  import Console from "./components/Console.svelte";
  import Toast from "./components/Toast.svelte";
  import Turtle from "./components/Turtle.svelte";
  import themeColor from "./storeThemes.js";
  import { PaneGroup, Pane, PaneResizer } from "paneforge";
</script>

<main class={$themeColor}>
  <Header />
  <div class="container-fluid p-0 m-0">
    <PaneGroup
      direction="horizontal"
      class="w-full"
      style="min-height: calc(100vh - 80px)"
    >
      <Pane defaultSize={50} minSize={30}>
        <ButtonBar />
        <PaneGroup direction="vertical" style="height: calc(100vh - 140px)">
          <Pane defaultSize={60} minSize={30}>
            <Textarea />
          </Pane>
          <PaneResizer class="relative flex" tabindex="-1">
            <div class="resizer-ver {$themeColor}"></div>
          </PaneResizer>
          <Pane defaultSize={35} minSize={30}>
            <Console />
          </Pane>
        </PaneGroup>
      </Pane>
      <PaneResizer class="relative flex" tabindex="-1">
        <div class="resizer-hor {$themeColor}"></div>
      </PaneResizer>
      <Pane defaultSize={50} minSize={30}>
        <Turtle />
        <InfoBar />
      </Pane>
    </PaneGroup>
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
    height: 100vh;
    &.dark {
      background-color: var(--bg-dark);
    }
    &.light {
      background-color: var(--bg-light);
    }
  }

  .container-fluid {
    height: calc(100vh - 80px);
  }

  .resizer-hor {
    width: 10px;
    height: 100%;
    cursor: ew-resize;
    z-index: 10;
    &.light {
      background: var(--ter-pri-light);
    }
    &.dark {
      background: var(--ter-pri-dark);
    }
  }

  .resizer-ver {
    height: 10px;
    cursor: ns-resize;
    &.light {
      background: var(--ter-pri-light);
    }
    &.dark {
      background: var(--ter-pri-dark);
    }
  }
</style>
