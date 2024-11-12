<script lang="js">
  export let logo;
</script>

<header class="header">
  <img src={logo} alt="Logo" class="logo" />
  <h1>Logo Playground</h1>
</header>

<style>
  .header {
    display: flex;
    align-items: center;
    background-color: #4caf50;
    color: white;
    padding: 10px;
    z-index: 10;
  }
  .logo {
    width: 50px;
    height: 50px;
    margin-right: 10px;
    margin-left: 20px;
  }
</style>
