import spacy
from textblob import TextBlob
from app.services.issue_classifier import classify_issue
from app.services.priority_engine import compute_priority

nlp_model = spacy.load("en_core_web_sm")

def analyze_text(text: str):
    doc = nlp_model(text)
    entities = [ent.text for ent in doc.ents]

    sentiment = TextBlob(text).sentiment.polarity
    issue = classify_issue(text)

    priority = compute_priority(
        issue["issue_type"],
        sentiment,
        text
    )

    return {
        "entities": list(set(entities)),
        "sentiment": sentiment,
        "issue": issue,
        "priority": priority
    }
