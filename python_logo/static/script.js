const element = document.getElementById("resizable");
const resizer = document.createElement("div");
const turtleCanvas = document.getElementById("turtlecanvas");
const imageCanvas = document.getElementById("imagecanvas");

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
 * Resizes the turtle canvas and image canvas to fit the right container.
 * @function resizeCanvas
 */
function resizeCanvas() {
  const container = document.querySelector(".right-container");
  const width = container.clientWidth;
  const height = container.clientHeight;

  turtleCanvas.width = width;
  turtleCanvas.height = height;
  imageCanvas.width = width;
  imageCanvas.height = height;
}

/**
 * Sends the code from the textarea to the server via a POST request.
 * The server processes the code and sends back the turtle commands.
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
      } else {
        return response.json();
      }
    })
    .then((data) => {
      if (data.commands) {
        data.commands.forEach((command) => {
          if (command.command === "forward") {
            forward(command.value);
          } else if (command.command === "right") {
            right(command.value);
          } else if (command.command === "left") {
            left(command.value);
          } else if (command.command === "backward") {
            backward(command.value);
          }
        });
      }
    })
    .catch((error) => console.error("Error:", error));
}
