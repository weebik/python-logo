<script>
  let { title, closeEvent, children } = $props();
</script>

<div class="modal fade show d-block" tabindex="-1" role="dialog">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="modalLabel">{title}</h5>
      </div>
      <div class="modal-body">
        {@render children()}
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" onclick={closeEvent}>
          Close
        </button>
      </div>
    </div>
  </div>
</div>
