def get_suggestion(mood):
    if "Positive" in mood:
        return "Keep going! Write one thing you're grateful for 🌱"
    elif "Negative" in mood:
        return "It's okay to feel this way. Try deep breathing 💙"
    else:
        return "Stay balanced and take care 🧘"
