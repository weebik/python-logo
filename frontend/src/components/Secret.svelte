<script>
  export let close;

  function handleClose() {
    close();
  }
</script>

<div
  class="modal fade show d-block"
  tabindex="-1"
  role="dialog"
  aria-labelledby="contactModalLabel"
  aria-hidden="true"
>
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="contactModalLabel">
          Nobody expects the CatGirl inquisition
        </h5>
        <button type="button" class="btn btn-secondary" on:click={handleClose}
          >Close</button
        >
      </div>
      <div class="modal-body w-100 p-0 m-0">
        <div
          class="tenor-gif-embed"
          data-postid="14887330"
          data-share-method="host"
          data-aspect-ratio="0.71875"
          data-width="100%"
        ></div>
        <script
          type="text/javascript"
          async
          src="https://tenor.com/embed.js"
        ></script>
      </div>
    </div>
  </div>
</div>
