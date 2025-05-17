# Spam Website Detector - Chrome Extension

## 📌 Overview
The **Spam Website Detector** is a Chrome extension that helps users identify whether a website is spam or not. The primary goal of this project is to develop a reliable and real-time phishing and spam website detection system that protects users from visiting malicious or harmful websites. The system integrates a machine learning model, specifically a Transformer-based model (like BERT), trained to classify websites as either "safe" (ham) or "spam" (phishing/malicious).
## 🚀 Features
- ✅ Detects spam and phishing websites in real-time.
- 🔍 Uses an intelligent filtering system to analyze URLs.
- ⚠️ Displays a warning for suspicious websites.
- 🛡️ Enhances browsing security and protects user data.

## 🛠️ Installation
1. **Install requirements.txt **: 
   - Run `pip install -r requirements.txt` in your terminal.
2. **Open Chrome and Go to Extensions**
   - Open `chrome://extensions/` in your Chrome browser.
   - Enable **Developer mode** (toggle in the top right corner).
3. **Load the Extension**
   - Click **Load unpacked**.
   - Select the downloaded/cloned project folder.
4. **Start Using!**
   - The extension will now analyze websites as you browse.
5. **Run Server Locally**
   - project_location
     ```sh
        - python server.py
     ```

## 🏗️ Project Structure
```
📂 spam-website-detector/
 ├── 📄 manifest.json  # Chrome extension manifest file
 ├── 📄 background.js  # Background script for processing URLs
 ├── 📄 popup.html     # User interface for the extension
 ├── 📄 popup.js       # JavaScript logic for popup
 ├── 📄 style.css      # Styles for the popup UI
 ├── 📄 icon.png       # Extension icon
 ├── 📄 README.md      # Documentation file
```

## 🖥️ How It Works
1. The extension continuously monitors the URLs of websites visited.
2. It checks the website against a **predefined spam database** or **AI-based model**.
3. If a website is flagged as spam, the user gets an alert/warning.
4. Optionally, users can manually report spam websites.

## 🔧 Technologies Used
- **JavaScript** (Background processing, API calls)
- **HTML & CSS** (Popup UI)
- **Chrome Extensions API** (Web request interception)

## 📌 Future Enhancements
- 📊 Machine Learning model integration for better accuracy.
- 🌎 Support for multiple browsers.
- 🔗 Community-based reporting system for spam detection.

## 🤝 Contributing
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Push to the branch and submit a PR.

## 📜 License
This project is licensed under the MIT License.

---
🚀 **Protect yourself from spam & phishing websites with this Chrome Extension!**

