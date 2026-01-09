import pandas as pd
from datetime import datetime
from suggestions import get_suggestion

# 🔁 Choose analyzer safely
try:
    from azure_mood_analyzer import analyze_mood_azure as analyze_mood
except Exception:
    from mood_analyzer import analyze_mood


def main():
    print("\n🧠 AI Mental Health Mood Tracker")
    print("--------------------------------")

    text = input("How are you feeling today?\n> ")

    mood, confidence = analyze_mood(text)
    suggestion = get_suggestion(mood)

    print(f"\nMood Detected: {mood}")
    print(f"Confidence: {confidence:.2f}")
    print(f"Suggestion: {suggestion}")

    log = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "text": text,
        "mood": mood,
        "confidence": confidence
    }

    df = pd.DataFrame([log])

    try:
        old = pd.read_csv("data/mood_log.csv")
        df = pd.concat([old, df])
    except FileNotFoundError:
        pass

    df.to_csv("data/mood_log.csv", index=False)


if __name__ == "__main__":
    main()
