<script lang="js">
  export let placeholder = "Type your code here...";
  export let value = "";
  export let id = "";
</script>

<div class="textbox">
  <textarea id={id} class="textarea" {placeholder} bind:value
  ></textarea>
</div>

<style>
  .textbox {
    display: flex;
    justify-content: center;
    width: 100%;
    height: 100%;
  }

  .textarea {
    border: none;
    width: 100%;
    height: 100%;
    resize: none;
    background-color: #1e1e1e;
    color: white;
    font-family: "Courier New", Courier, monospace;
    padding: 10px;
  }

  .textarea:focus {
    outline: none;
  }
</style>
