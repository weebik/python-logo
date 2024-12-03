<script module>
  import { toast } from "@zerodevx/svelte-toast";

  export function toastSuccess(message) {
    toast.push(message, {
      theme: {
        "--toastWidth": "24rem",
        "--toastBackground": "#74e344",
        "--toastcolor": "white",
        "--toastBorderRadius": "1rem",
        "--toastBarBackground": "darkGreen",
        "--toastPadding": "0.75rem",
        "font-family": "Ubuntu, sans-serif",
      },
    });
  }

  export function toastError(message) {
    toast.push(message, {
      theme: {
        "--toastWidth": "24rem",
        "--toastBackground": "#ff3931",
        "--toastcolor": "white",
        "--toastBorderRadius": "1rem",
        "--toastBarBackground": "darkRed",
        "--toastPadding": "0.75rem",
        "font-family": "Ubuntu, sans-serif",
      },
    });
  }
</script>

<script>
  import { SvelteToast } from "@zerodevx/svelte-toast";
</script>

<SvelteToast />
