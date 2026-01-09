from transformers import pipeline

classifier = pipeline("sentiment-analysis")

def analyze_mood(text):
    result = classifier(text)[0]
    label = result["label"]
    score = result["score"]

    if label == "POSITIVE":
        if score > 0.95:
            return "😄 Happy", score
        elif score > 0.85:
            return "😃 Excited", score
        else:
            return "😌 Calm", score
    else:
        if score > 0.95:
            return "😞 Depressed", score
        elif score > 0.85:
            return "😨 Anxious", score
        else:
            return "😢 Sad", score
