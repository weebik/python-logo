<script module>
  let code = $state("");
  let console = $state("");
  let logs = $state([]);
  let consoleContainerEl;

  export function getCode() {
    return code;
  }

  export function setCode(newCode) {
    code = newCode;
  }

  export function setConsole(newConsole) {
    console = newConsole;
  }

  function scrollConsoleToBottom() {
    if (consoleContainerEl) {
      consoleContainerEl.scrollTop = consoleContainerEl.scrollHeight;
    }
  }

  export function logToConsole(message) {
    logs = [...logs, message];

    if (logs.length > 1000) {
      logs = logs.slice(-1000);
    }

    setTimeout(() => scrollConsoleToBottom(), 0);
  }
</script>

<script>
  import themeColor from "../storeThemes.js";

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

<div class="m-5 h-100">
  <div class="textarea-container">
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
  <div class="console-container mt-3">
    <div class="console {$themeColor} p-3" bind:this={consoleContainerEl}>
      {#each logs as log}
        <p>> {log}</p>
      {/each}
    </div>
  </div>
</div>

<style>
  .textarea-container {
    height: 100%;
    max-height: calc(80vh - 140px);
    display: flex;
    border-radius: 1rem;
  }

  .console-container {
    height: 100%;
    height: 10vh;
    display: flex;
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
    width: 100%;
    border: none;
    resize: none;
    font-family: "Ubuntu Mono", monospace;
    border-radius: 1rem;
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
</style>
