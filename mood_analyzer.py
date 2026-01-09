from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_mood(text):
    result = sentiment_pipeline(text)[0]
    label = result["label"]
    score = result["score"]

    if label == "POSITIVE":
        return "Positive 😊", score
    elif label == "NEGATIVE":
        return "Negative 😔", score
    else:
        return "Neutral 😐", score
