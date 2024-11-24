<script>
  import Modal from "./Modal.svelte";

  let showLicenseModal = false;
  let showContactModal = false;
</script>

<div class="info-bar d-flex align-items-center justify-content-end w-100">
  <div class="d-flex gap-4 p-0 me-5">
    <button
      class="p-0 m-0 text-nowrap"
      title="License"
      onclick={() => (showLicenseModal = true)}
    >
      <img class="pe-1" src="/license.svg" alt="License" />
      License
    </button>
    <button
      class="p-0 m-0 text-nowrap"
      title="Contact"
      onclick={() => (showContactModal = true)}
    >
      <img class="pe-1" src="/contact.svg" alt="Contact" />
      Contact
    </button>
    <a
      href="https://github.com/YarynaRachkevych1/python-logo"
      target="_blank"
      rel="noopener noreferrer"
    >
      <button class="p-0 m-0 text-nowrap" title="Visit our GitHub">
        <img class="pe-1" src="/github.svg" alt="GitHub" />
        Visit our GitHub
      </button>
    </a>
  </div>
</div>

{#if showLicenseModal}
  <Modal title="License" closeEvent={() => (showLicenseModal = false)}>
    This software is licensed under the MIT license.
  </Modal>
{/if}

{#if showContactModal}
  <Modal title="Contact us" closeEvent={() => (showContactModal = false)}>
    If you have any questions or suggestions, feel free to contact us:
    <ul>
      <li>Krystian Ćwikliński: krystian.samaa@gmail.com</li>
      <li>Mikołaj Kalitka: mkalitka@gmail.com</li>
      <li>Yaryna Rachkevych: yaryna@gmail.com</li>
      <li>Magda Tytoń: magda@gmail.com</li>
    </ul>
  </Modal>
{/if}

<style>
  .info-bar {
    background-image: url("/info-bar.svg");
    height: 60px;
    z-index: 1;
  }
  button {
    user-select: none;
    border: none;
    cursor: pointer;
    background-color: transparent;
    transition:
      scale 0.2s,
      filter 0.05s;
    filter: invert(90%) sepia(3%) saturate(1480%) hue-rotate(53deg)
      brightness(113%) contrast(106%);
    font-family: "Ubuntu", sans-serif;
    font-weight: bold;
  }
  button:hover {
    scale: 1.1;
    filter: invert(90%) sepia(16%) saturate(674%) hue-rotate(62deg)
      brightness(103%) contrast(96%);
  }
  button:active {
    scale: 1.05;
    filter: invert(90%) sepia(16%) saturate(674%) hue-rotate(62deg)
      brightness(113%) contrast(96%);
  }
</style>
