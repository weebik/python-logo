<script module>
  import themeColor from "../storeThemes.js";

  let code = $state("");
  let textAreaEl;
  let numberLinesEl;

  /**
   * Get the code from the textarea
   */
  export function getCode() {
    return code;
  }

  /**
   * Sets the code in the textarea
   * @param newCode
   */
  export function setCode(newCode) {
    code = newCode;
  }

  /**
   * Get the line numbers for the textarea
   * @param content
   */
  function getLineNumbers(content) {
    const lines = content.split("\n").length;
    return Array.from({ length: lines }, (_, i) => i + 1).join("\n");
  }

  /**
   * Sync the scroll position of the textarea and line numbers
   */
  function syncScroll() {
    if (numberLinesEl && textAreaEl) {
      numberLinesEl.scrollTop = textAreaEl.scrollTop;
    }
  }
</script>

<div class="container-fluid d-flex flex-column h-100 m-0 p-0">
  <div class="textarea-container p-5 h-100">
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
</div>

<style>
  .textarea-container {
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
</style>
