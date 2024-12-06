<script module>
  let code = $state("");

  export function getCode() {
    return code;
  }

  export function setCode(newCode) {
    code = newCode;
  }

  function getLineNumbers(content) {
    const lines = content.split("\n").length;
    return Array.from({ length: lines }, (_, i) => i + 1).join("\n");
  }

  let textAreaEl;
  let numberLinesEl;

  function syncScroll() {
    if (numberLinesEl && textAreaEl) {
      numberLinesEl.scrollTop = textAreaEl.scrollTop;
    }
  }
</script>

<div class="m-5 h-100">
  <div class="textarea-container">
    <div
      bind:this={numberLinesEl}
      class="line-numbers py-4"
      style="background-color: #0f2534;
      user-select: none;
    color: #627d90;"
      role="presentation"
      onmouseover={() => (numberLinesEl.style.overflow = "hidden")}
      onfocus={() => (numberLinesEl.style.overflow = "hidden")}
      onmouseleave={() => (numberLinesEl.style.overflow = "auto")}
      onblur={() => (numberLinesEl.style.overflow = "auto")}
    >
      <pre class="px-3">{getLineNumbers(code)}</pre>
    </div>
    <textarea
      bind:this={textAreaEl}
      class="form-control h-100 shadow-none py-4"
      style="color: #cae5be; background-color: #153246;"
      placeholder="Type your code here..."
      bind:value={code}
      onscroll={syncScroll}
    ></textarea>
  </div>
</div>

<style>
  .textarea-container {
    max-height: calc(90vh - 140px);
    display: flex;
    height: 100%;
    background-color: #153246;
    border-radius: 1rem;
    overflow: hidden;
  }

  .line-numbers {
    border-top-left-radius: 1rem;
    border-bottom-left-radius: 1rem;
    /* disable scrollbar */
    -ms-overflow-style: none;
    scrollbar-width: none;
    &::-webkit-scrollbar {
      display: none;
    }
  }

  pre {
    line-height: 1.5;
    width: 100%;
    color: #627d90;
    text-align: right;
    user-select: none;
    font-size: large;
    /* disable scrollbar */
    -ms-overflow-style: none;
    scrollbar-width: none;
    &::-webkit-scrollbar {
      display: none;
    }
  }

  textarea {
    border: none;
    resize: none;
    font-family: "Ubuntu Mono", monospace;
    border-radius: 1rem;
    font-size: large;
    line-height: 1.5;
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
