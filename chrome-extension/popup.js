document.getElementById("checkPhishing").addEventListener("click", function () {
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        let currentUrl = tabs[0].url;
        checkPhishing(currentUrl);
    });
});

function checkPhishing(url) {
    fetch("http://127.0.0.1:5000/check", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ url: url })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = `Result: ${data.result}`;
    })
    .catch(error => {
        document.getElementById("result").innerText = "Error connecting to server.";
        console.error("Error:", error);
    });
}
