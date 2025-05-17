document.getElementById("checkBtn").addEventListener("click", async () => {
    let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    const url = tab.url;
  
    fetch("http://127.0.0.1:5000/check", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ url })
    })
    .then(res => res.json())
    .then(data => {
      document.getElementById("result").innerText = data.result;
    })
    .catch(err => {
      document.getElementById("result").innerText = "Error connecting to server.";
      console.error(err);
    });
  });
  