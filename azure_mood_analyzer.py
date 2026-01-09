import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("AZURE_ENDPOINT")
key = os.getenv("AZURE_KEY")

client = TextAnalyticsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)

def analyze_mood_azure(text):
    result = client.analyze_sentiment([text])[0]
    sentiment = result.sentiment

    if sentiment == "positive":
        return "Positive 😊", result.confidence_scores.positive
    elif sentiment == "negative":
        return "Negative 😔", result.confidence_scores.negative
    else:
        return "Neutral 😐", result.confidence_scores.neutral
