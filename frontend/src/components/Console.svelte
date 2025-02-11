<script module>
  import themeColor from "../storeThemes.js";

  let logs = $state([]);
  let consoleContainerEl;

  /**
   * Handle logging to console
   * Max 25 logs
   * @param {string} message
   */
  export function logToConsole(message) {
    logs = [...logs, message];

    if (logs.length > 25) {
      logs = logs.slice(-25);
    }

    setTimeout(() => scrollConsoleToBottom(), 0);
  }

  /**
   * Clears console logs
   */
  function clearConsole() {
    logs.length = 0;
    logs = [];
    logToConsole("Console cleared!");
  }

  /**
   * Automatically scroll console to bottom
   */
  function scrollConsoleToBottom() {
    if (consoleContainerEl) {
      consoleContainerEl.scrollTop = consoleContainerEl.scrollHeight;
    }
  }

  logToConsole("Console initialized.");
</script>

<div class="console-container p-5 h-100">
  <div class="console-btns {$themeColor} d-flex justify-content-end">
    <button class="clear-btn {$themeColor}" onclick={clearConsole}>clear</button
    >
  </div>
  <div class="console px-3 {$themeColor}" bind:this={consoleContainerEl}>
    {#each logs as log}
      <p>> {log}</p>
    {/each}
  </div>
</div>

<style>
  .console-container {
    border-radius: 1rem;
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
