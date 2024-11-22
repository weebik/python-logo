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
  aria-labelledby="licenseModalLabel"
  aria-hidden="true"
>
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="licenseModalLabel">License</h5>

      </div>
      <div class="modal-body">
        This software is licensed under the MIT License.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" on:click={handleClose}
          >Close</button
        >
      </div>
    </div>
  </div>
</div>
