<script module>
  let code = $state("");
  let console = $state("");

  export function getCode() {
    return code;
  }

  export function setCode(newCode) {
    code = newCode;
  }

  export function setConsole(newConsole) {
    console = newConsole;
  }
</script>

<script>
  let textAreaEl;
  let numberLinesEl;
  let logs = $state([]);

  function getLineNumbers(content) {
    const lines = content.split("\n").length;
    return Array.from({ length: lines }, (_, i) => i + 1).join("\n");
  }

  function syncScroll() {
    if (numberLinesEl && textAreaEl) {
      numberLinesEl.scrollTop = textAreaEl.scrollTop;
    }
  }

  function logToConsole(message) {
    logs = [...logs, message];
  }

  logToConsole("Console initialized.");
</script>

<div class="m-5 h-100">
  <div class="textarea-container">
    <div
      class="line-numbers py-4"
      role="presentation"
      bind:this={numberLinesEl}
    >
      <pre>{getLineNumbers(code)}</pre>
    </div>
    <textarea
      class="form-control h-100 shadow-none py-4"
      style="color: #cae5be;"
      placeholder="Type your code here..."
      spellcheck="false"
      onscroll={syncScroll}
      bind:this={textAreaEl}
      bind:value={code}
    ></textarea>
  </div>
  <div class="console-container mt-3">
    <div class="console p-3">
      {#each logs as log}
        <p>> {log}</p>
      {/each}
    </div>
  </div>
</div>

<style>
  .textarea-container {
    background-color: #153246;
    height: 100%;
    max-height: calc(80vh - 140px);
    display: flex;
    border-radius: 1rem;
  }

  .console-container {
    background-color: #0f2534;
    height: 100%;
    height: 10vh;
    display: flex;
    border-radius: 1rem;
  }

  .line-numbers {
    background-color: #0f2534;
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
  }

  pre {
    line-height: 1.5;
    color: #627d90;
    user-select: none;
    font-size: large;
  }

  textarea {
    background-color: #153246;
    border: none;
    resize: none;
    font-family: "Ubuntu Mono", monospace;
    border-radius: 1rem;
    font-size: large;
    line-height: 1.5;
  }

  .console {
    background-color: #0f2534;
    border: none;
    resize: none;
    font-family: "Ubuntu Mono", monospace;
    border-radius: 1rem;
    font-size: large;
    line-height: 1.5;
    p {
      margin: 0;
      padding: 0;
      color: #627d90;
      font-size: small;
    }
  }

  textarea::placeholder {
    user-select: none;
    color: #627d90;
  }

  textarea:focus {
    outline: none;
    background-color: #153246;
  }
</style>
