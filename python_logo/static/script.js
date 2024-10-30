var element = document.getElementById("resizable");
var resizer = document.createElement("div");
resizer.className = "resizer";
element.appendChild(resizer);
resizer.addEventListener("mousedown", initResize, false);

let tabCount = 0;
let currentTabId = null;

document.addEventListener("DOMContentLoaded", () => {
  addTab();
});

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
  if (currentTabId) {
    const code = document.getElementById(currentTabId).value;
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
}

// !!!experimental!!!

/**
 * Add new tab and set it as active
 * @function addTab
 */
function addTab() {
  tabCount++;
  const tabId = `tab${tabCount}`;
  const tabList = document.getElementById("tabList");
  const tabContentContainer = document.getElementById("tabContentContainer");

  const newTabButton = document.createElement("li");
  newTabButton.classList.add("tab");
  newTabButton.innerHTML = `Tab ${tabCount} <span class="close-btn" onclick="removeTab('${tabId}')">×</span>`;
  newTabButton.onclick = (e) => {
    if (!e.target.classList.contains("close-btn")) setActiveTab(tabId);
  };
  newTabButton.id = `${tabId}-button`;

  tabList.insertBefore(newTabButton, tabList.lastElementChild);

  const newTextArea = document.createElement("textarea");
  newTextArea.id = tabId;
  newTextArea.className = "textarea";
  newTextArea.placeholder = `Type your code in Terminal ${tabCount}`;
  newTextArea.style.display = "none";
  tabContentContainer.appendChild(newTextArea);
  setActiveTab(tabId);
}

/**
 * Set tab as active and display its content
 * @function setActiveTab
 * @param {string} tabId
 */
function setActiveTab(tabId) {
  if (currentTabId) {
    document.getElementById(currentTabId).style.display = "none";
    document
      .getElementById(`${currentTabId}-button`)
      .classList.remove("active");
  }
  document.getElementById(tabId).style.display = "block";
  document.getElementById(`${tabId}-button`).classList.add("active");
  currentTabId = tabId;
}

/**
 * Delete active tab and content, find new tab and set as active
 * @function removeTab
 * @param {string} tabId
 */
function removeTab(tabId) {
  const tabButton = document.getElementById(`${tabId}-button`);
  const tabContent = document.getElementById(tabId);
  const tabList = document.getElementById("tabList");

  if (currentTabId === tabId) {
    const remainingTabs = tabList.querySelectorAll("li.tab");
    let nextTabId = null;

    for (const tab of remainingTabs) {
      const id = tab.id.replace("-button", "");
      if (id !== tabId) {
        nextTabId = id;
        break;
      }
    }
    if (nextTabId) {
      setActiveTab(nextTabId);
    } else {
      addTab();
    }
  }
  tabButton.remove();
  tabContent.remove();
}
