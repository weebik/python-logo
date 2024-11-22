<script>
  import { onMount } from "svelte";
  import LicenseModal from "./LicenseModal.svelte";
  import ContactModal from "./ContactModal.svelte";

  let showLicenseModal = false;
  let showContactModal = false;

  function openLicenseModal() {
    showLicenseModal = true;
  }

  function openContactModal() {
    showContactModal = true;
  }

  function closeModal() {
    showLicenseModal = false;
    showContactModal = false;
  }
</script>

<div
  class="d-flex align-items-center justify-content-end w-100"
  style="background-image: url('/infoBar.svg'); height: 60px;"
>
  <div class="d-flex gap-4 p-0 me-5">
    <button class="p-0 m-0 text-nowrap" on:click={openLicenseModal}>
      <img class="pe-1" src="/license.svg" alt="License" />
      License
    </button>
    <button class="p-0 m-0 text-nowrap" on:click={openContactModal}>
      <img
        class="pe-1"
        style="background-color: transparent;"
        src="/contact.svg"
        alt="Contact"
      />
      Contact
    </button>
    <a
      href="https://github.com/YarynaRachkevych1/python-logo"
      target="_blank"
      rel="noopener noreferrer"
    >
      <button class="p-0 m-0 text-nowrap">
        <img class="pe-1" src="/github.svg" alt="Github" />
        Visit our GitHub
      </button>
    </a>
  </div>
</div>
{#if showLicenseModal}
  <LicenseModal on:close={closeModal} close={closeModal} />
{/if}

{#if showContactModal}
  <ContactModal on:close={closeModal} close={closeModal}/>
{/if}

<style>
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
