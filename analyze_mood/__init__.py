import json
import os
import azure.functions as func
from suggestions import get_suggestion

try:
    from azure_mood_analyzer import analyze_mood_azure as analyze_mood
except Exception:
    from mood_analyzer import analyze_mood


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        body = req.get_json()
        text = body.get("text", "")
    except Exception:
        return func.HttpResponse(
            "Invalid JSON",
            status_code=400
        )

    if not text:
        return func.HttpResponse(
            "Text is required",
            status_code=400
        )

    mood, confidence = analyze_mood(text)
    suggestion = get_suggestion(mood)

    return func.HttpResponse(
        json.dumps({
            "mood": mood,
            "confidence": round(float(confidence), 2),
            "suggestion": suggestion
        }),
        mimetype="application/json"
    )
