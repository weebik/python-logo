var element = document.getElementById("resizable");
var resizer = document.createElement("div");
resizer.className = "resizer";
element.appendChild(resizer);
resizer.addEventListener("mousedown", initResize, false);

/**
 * Initiates the resizing process by adding mouse event listeners.
 * @function initResize
 * @param {MouseEvent} e - The mouse event that triggers resizing.
 */
function initResize(e) {
  window.addEventListener("mousemove", startResizing, false);
  window.addEventListener("mouseup", stopResizing, false);
}

/**
 * Resizes the element's width based on the current mouse position.
 * @function startResizing
 * @param {MouseEvent} e - The mouse event with the current position.
 */
function startResizing(e) {
  element.style.width = e.clientX - element.offsetLeft + "px";
}

/**
 * Stops the resizing process by removing event listeners.
 * @function stopResizing
 * @param {MouseEvent} e - The mouse event that triggers stopping the resizing.
 */
function stopResizing(e) {
  window.removeEventListener("mousemove", startResizing, false);
  window.removeEventListener("mouseup", stopResizing, false);
}

/**
 * Sends the code from the textarea to the server via a POST request.
 * @function sendCode
 */
function sendCode() {
  const code = document.getElementById("codeTextarea").value;

  fetch("/", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: new URLSearchParams({ code: code }),
  })
    .then((response) => {
      if (response.redirected) {
        window.location.href = response.url;
      }
    })
    .catch((error) => console.error("Error:", error));
}
