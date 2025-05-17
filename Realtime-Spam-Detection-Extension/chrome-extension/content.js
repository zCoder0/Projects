(async function checkPhishing() {
  const currentUrl = window.location.href;

  // Avoid checking internal or extension URLs
  if (
    currentUrl.startsWith("chrome://") ||
    currentUrl.startsWith("chrome-extension://") ||
    currentUrl.includes("block.html")
  ) {
    return;
  }

  try {
    const response = await fetch("http://127.0.0.1:5000/check", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ url: currentUrl })
    });

    const data = await response.json();

    if (data.result.toLowerCase().includes("spam")) {
      // Redirect to block page
      window.location.replace(chrome.runtime.getURL("block.html"));
    } else {
      // Show safe popup message
      showSafePopup();
    }
  } catch (err) {
    console.error("Phishing check failed:", err);
  }
})();

// Function to create and show a popup message
function showSafePopup() {
  const popup = document.createElement("div");
  popup.textContent = "✅ This website is safe!";
  popup.style.position = "fixed";
  popup.style.top = "10px";
  popup.style.right = "10px";
  popup.style.backgroundColor = "#4CAF50";
  popup.style.color = "white";
  popup.style.padding = "10px 20px";
  popup.style.borderRadius = "5px";
  popup.style.boxShadow = "0 2px 6px rgba(0,0,0,0.3)";
  popup.style.zIndex = "999999";
  popup.style.fontSize = "16px";

  document.body.appendChild(popup);

  // Remove popup after 5 seconds
  setTimeout(() => {
    popup.remove();
  }, 5000);
}
