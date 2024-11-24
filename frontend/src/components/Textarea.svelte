<script lang="js">
  export let placeholder = "Type your code here...";
  export let value = "";
  export let id = "";
</script>

<div class="m-5 h-100">
  <textarea
    class="form-control h-100 shadow-none p-4"
    style="color: #cae5be; background-color: #153246;"
    {id}
    {placeholder}
    bind:value
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
