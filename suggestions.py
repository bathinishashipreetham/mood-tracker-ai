def get_suggestion(mood):
    suggestions = {
        "😄 Happy": "Keep doing what makes you happy 🌟",
        "😃 Excited": "Channel this energy into something creative 🚀",
        "😌 Calm": "Maintain this balance with mindfulness 🧘",
        "😢 Sad": "Talk to someone you trust 💬",
        "😨 Anxious": "Try deep breathing for 2 minutes 🌬️",
        "😞 Depressed": "You’re not alone. Reach out for help ❤️",
        "😐 Neutral": "Check in with yourself and rest 🛌",
        "😠 Angry": "Pause and step away for a moment 🔄"
    }

    return suggestions.get(mood, "Take care of yourself 💙")
