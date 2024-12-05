<script module>
  let code = $state("");

  export function getCode() {
    return code;
  }

  export function setCode(newCode) {
    code = newCode;
  }
</script>

<div class="m-5 h-100">
  <textarea
    class="form-control h-100 shadow-none p-4"
    style="color: #cae5be; background-color: #153246;"
    placeholder="Type your code here..."
    bind:value={code}
  ></textarea>
</div>

<style>
  textarea {
    border: none;
    resize: none;
    font-family: "Ubuntu Mono", monospace;
    border-radius: 1rem;
    font-size: large;
    transition: all 0.3s;
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
