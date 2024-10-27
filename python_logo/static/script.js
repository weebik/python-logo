// function to resize textarea
var element = document.getElementById('resizable');
var resizer = document.createElement('div');
resizer.className = 'resizer';

element.appendChild(resizer);
resizer.addEventListener('mousedown', initResize, false);

function initResize(e) {
   window.addEventListener('mousemove', startResizing, false);
   window.addEventListener('mouseup', stopResizing, false);
}

function startResizing(e) {
   element.style.width = (e.clientX - element.offsetLeft) + 'px';
}

function stopResizing(e) {
    window.removeEventListener('mousemove', startResizing, false);
    window.removeEventListener('mouseup', stopResizing, false);
}

// Sending code from text area to backend server
function sendCode() {
   const code = document.getElementById('codeTextarea').value;

   fetch("/", {
       method: "POST",
       headers: {
           "Content-Type": "application/x-www-form-urlencoded"
       },
       body: new URLSearchParams({ code: code })
   })
   .then(response => {
       if (response.redirected) {
           window.location.href = response.url;
       }
   })
   .catch(error => console.error("Error:", error));
}
