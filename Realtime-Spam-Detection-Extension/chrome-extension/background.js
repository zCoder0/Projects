chrome.webRequest.onBeforeRequest.addListener(
    async function (details) {
      const url = details.url;
  
      // Don't check localhost or internal Chrome pages
      if (url.startsWith("chrome://") || url.startsWith("chrome-extension://")) {
        return {};
      }
  
      try {
        const response = await fetch("http://127.0.0.1:5000/check", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ url: url })
        });
  
        const data = await response.json();
  
        if (data.result.includes("SPAM")) {
          return {
            redirectUrl: chrome.runtime.getURL("block.html")
          };
        }
      } catch (err) {
        console.error("Failed to check spam:", err);
      }
  
      return {}; // allow normally
    },
    { urls: ["<all_urls>"] },
    ["blocking"]
  );
  