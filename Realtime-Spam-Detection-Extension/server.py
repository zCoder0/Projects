from flask import Flask, request, jsonify
from src.components.data_integstion import ScrapedData
import warnings

warnings.filterwarnings("ignore")
from flask_cors import CORS



app = Flask(__name__)
CORS(app)  
sc_data = ScrapedData()

@app.route("/check", methods=["POST"])
def check_url():
    data = request.json
    url = data.get("url", "")
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    status = sc_data.check_url_for_spam(url)
    result = "SPAM" if status == "SPAM" else "HAM"
    return jsonify({"url": url, "result": result})

if __name__ == "__main__":
    app.run(debug=True)
