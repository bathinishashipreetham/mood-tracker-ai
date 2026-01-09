from flask import Flask, request, jsonify, render_template
from suggestions import get_suggestion

try:
    from azure_mood_analyzer import analyze_mood_azure as analyze_mood
except Exception:
    from mood_analyzer import analyze_mood

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json() or {}
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "Text is required"}), 400

    mood, confidence = analyze_mood(text)
    suggestion = get_suggestion(mood)

    return jsonify({
        "mood": mood,
        "confidence": round(float(confidence), 2),
        "suggestion": suggestion
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
