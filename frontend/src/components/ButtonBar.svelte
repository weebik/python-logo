<script lang="js">
  import { createEventDispatcher } from "svelte";
  const dispatch = createEventDispatcher();

  function handleRunClick() {
    dispatch("run"); // Emit a 'run' event when the "Run" button is clicked
  }
</script>

<div class="button-bar">
  <button on:click={handleRunClick}>Run</button>
  <button>Stop</button>
</div>

<style>
  .button-bar {
    display: flex;
    justify-content: center;
    padding: 10px;
    gap: 10px;
    background-color: #1e1e1e;
  }

  .button-bar button {
    padding: 10px 20px;
    border: none;
    background-color: #4caf50;
    color: white;
    cursor: pointer;
    border-radius: 5px;
    font-size: 16px;
    transition: background-color 0.3s;
  }

  .button-bar button:hover {
    background-color: #45a049;
  }

  .button-bar button:active {
    background-color: #5fb83c;
  }
</style>
