<script module>
  import themeColor from "../storeThemes.js";

  let code = $state("");
  let logs = $state([]);
  let consoleContainerEl;
  let textAreaHeight = $state(70);
  let consoleHeight = $state(30);
  let isResizing = false;

  export function getCode() {
    return code;
  }

  export function setCode(newCode) {
    code = newCode;
  }

  export function logToConsole(message) {
    logs = [...logs, message];

    if (logs.length > 25) {
      logs = logs.slice(-25);
    }

    setTimeout(() => scrollConsoleToBottom(), 0);
  }

  function clearConsole() {
    logs.length = 0;
    logs = [];
    logToConsole("Console cleared!");
  }

  function scrollConsoleToBottom() {
    if (consoleContainerEl) {
      consoleContainerEl.scrollTop = consoleContainerEl.scrollHeight;
    }
  }

  function startResizing(event) {
    isResizing = true;
    document.addEventListener("mousemove", resize, { passive: true });
    document.addEventListener("mouseup", stopResizing);
  }

  function resize(event) {
    if (!isResizing) return;
    const containerHeight =
      document.querySelector(".container-fluid").clientHeight;
    const newHeight = Math.max(
      30,
      Math.min(75, (event.clientY / containerHeight) * 100),
    );
    textAreaHeight = newHeight;
    consoleHeight = 100 - newHeight;
  }

  function stopResizing() {
    isResizing = false;
    document.removeEventListener("mousemove", resize);
    document.removeEventListener("mouseup", stopResizing);
  }

  let textAreaEl;
  let numberLinesEl;

  function getLineNumbers(content) {
    const lines = content.split("\n").length;
    return Array.from({ length: lines }, (_, i) => i + 1).join("\n");
  }

  function syncScroll() {
    if (numberLinesEl && textAreaEl) {
      numberLinesEl.scrollTop = textAreaEl.scrollTop;
    }
  }

  logToConsole("Console initialized.");
</script>

<div class="container-fluid d-flex flex-column h-100 m-0 p-0">
  <div class="textarea-container p-5" style="height: {textAreaHeight}%">
    <div
      class="line-numbers {$themeColor} py-4"
      role="presentation"
      bind:this={numberLinesEl}
    >
      <pre class={$themeColor}>{getLineNumbers(code)}</pre>
    </div>
    <textarea
      class="form-control {$themeColor} h-100 shadow-none py-4"
      placeholder="Type your code here..."
      spellcheck="false"
      onscroll={syncScroll}
      bind:this={textAreaEl}
      bind:value={code}
    ></textarea>
  </div>
  <!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
  <div
    class="resizer {$themeColor}"
    onmousedown={startResizing}
    role="separator"
    aria-orientation="vertical"
  ></div>
  <div class="console-container p-5" style="height: {consoleHeight}%">
    <div class="console-btns {$themeColor} d-flex justify-content-end">
      <button class="clear-btn {$themeColor}" onclick={clearConsole}
        >clear</button
      >
    </div>
    <div class="console px-3 {$themeColor}" bind:this={consoleContainerEl}>
      {#each logs as log}
        <p>> {log}</p>
      {/each}
    </div>
  </div>
</div>

<style>
  .resizer {
    height: 10px;
    width: 100%;
    cursor: ns-resize;
    &.light {
      background: var(--ter-pri-light);
    }
    &.dark {
      background: var(--ter-pri-dark);
    }
  }

  .textarea-container {
    display: flex;
    border-radius: 1rem;
  }

  .console-container {
    border-radius: 1rem;
  }

  .line-numbers {
    border-top-left-radius: 1rem;
    border-bottom-left-radius: 1rem;
    width: 42px;
    max-width: 42px;
    text-align: center;
    overflow: hidden;
    /* disable scrollbar */
    -ms-overflow-style: none;
    scrollbar-width: none;
    &::-webkit-scrollbar {
      display: none;
    }
    &.light {
      background-color: var(--ter-sec-light);
    }
    &.dark {
      background-color: var(--ter-sec-dark);
    }
  }

  pre {
    line-height: 1.5;
    user-select: none;
    font-size: large;
    &.light {
      color: var(--text-light);
    }
    &.dark {
      color: var(--placeholder-dark);
    }
  }

  textarea {
    border: none;
    resize: none;
    font-family: "Ubuntu Mono", monospace;
    border-radius: 0;
    border-top-right-radius: 1rem;
    border-bottom-right-radius: 1rem;
    font-size: large;
    line-height: 1.5;
    &:focus {
      outline: none;
    }
    &::placeholder {
      user-select: none;
    }
    &.light {
      background-color: var(--ter-pri-light);
      color: var(--text-light);
      &::placeholder {
        color: var(--placeholder-light);
      }
    }
    &.dark {
      background-color: var(--ter-pri-dark);
      color: var(--text-dark);
      &::placeholder {
        color: var(--placeholder-dark);
      }
    }
  }

  .console {
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 100%;
    border: none;
    resize: none;
    font-family: "Ubuntu Mono", monospace;
    border-bottom-left-radius: 1rem;
    border-bottom-right-radius: 1rem;
    font-size: large;
    line-height: 1.5;
    overflow-y: auto;
    p {
      margin: 0;
      padding: 0;
      font-size: small;
    }
    &.light {
      background-color: var(--ter-sec-light);
      p {
        color: var(--text-light);
      }
    }
    &.dark {
      background-color: var(--ter-sec-dark);
      p {
        color: var(--placeholder-dark);
      }
    }
  }
  .console-btns {
    border-top-left-radius: 1rem;
    border-top-right-radius: 1rem;
    &.light {
      background-color: var(--ter-sec-light);
    }
    &.dark {
      background-color: var(--ter-sec-dark);
    }
  }
  .clear-btn {
    position: relative;
    width: 50px;
    font-size: small;
    border: none;
    border-top-right-radius: 1rem;
    border-bottom-right-radius: 0.5rem;
    border-bottom-left-radius: 0.5rem;
    border-top-left-radius: 0.5rem;
    cursor: pointer;
    &:focus {
      outline: none;
    }
    &.light {
      background-color: var(--ter-pri-light);
      color: var(--text-light);
    }
    &.dark {
      background-color: var(--ter-pri-light);
      color: var(--text-light);
    }
  }
</style>
