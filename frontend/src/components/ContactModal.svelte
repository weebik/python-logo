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
        <h5 class="modal-title" id="contactModalLabel">Contact Us</h5>
      </div>
      <div class="modal-body">
        If you have any questions or suggestions, feel free to contact us:
        <ul>
          <li>Krystian Ćwikliński: krystian.samaa@gmail.com</li>
          <li>Mikołaj Kalitka: mkalitka@gmail.com</li>
          <li>Yaryna Rachkevych: yaryna@gmail.com</li>
          <li>Magda Tytoń: magda@gmail.com</li>
        </ul>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" on:click={handleClose}
          >Close</button
        >
      </div>
    </div>
  </div>
</div>
