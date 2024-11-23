<script lang="js">
  import Secret from "./Secret.svelte";
  let showSecretModal = false;
  function openSecretModal() {
    showSecretModal = true;
  }
  function closeSecretModal() {
    showSecretModal = false;
  }
</script>

<header
  class="d-flex w-100 justify-content-center align-items-center user-select-none"
  style="background: linear-gradient(90deg, #70F1C9 20%, #26B1B7 100%);
  font-family: Ubuntu, sans-serif;
  color: white;
  height: 80px;
  z-index: 10;"
>
  <img
    class="m-1 user-select-none"
    alt="Logo"
    src="/logo.png"
    style="width: 60px;height: 60px;"
  />
  <h1 style="font-weight: bold;margin: 5px;">Logo Playground</h1>
  <button class="secret" on:click={openSecretModal}>W</button>
</header>
{#if showSecretModal}
  <Secret on:close={closeSecretModal} close={closeSecretModal} />
{/if}

<style>
  .secret {
    cursor: default;
    border: none;
    position: absolute;
    left: 0;
    width: 10px;
    color: transparent;
    background-color: transparent;
    right: 0;
    z-index: 11;
  }
</style>
