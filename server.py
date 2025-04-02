from flask import Flask, request, jsonify
import pickle as pkl
import warnings

warnings.filterwarnings("ignore")

app = Flask(__name__)

# Load ML model
with open('Models/phishing_model.pkl', 'rb') as f:
    model = pkl.load(f)
with open("Models/phishing_vectorizer.pkl", "rb") as f:
    vectorizer = pkl.load(f)

@app.route("/check", methods=["POST"])
def check_url():
    data = request.json
    url = data.get("url", "")

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    test_vector = vectorizer.transform([url])
    result = "⚠ WARNING! This URL is a sapam " if model.predict(test_vector) else "it safe site"

    return jsonify({"url": url, "result": result})

if __name__ == "__main__":
    app.run(debug=True)
