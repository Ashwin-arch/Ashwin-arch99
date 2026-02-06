import spacy
from textblob import TextBlob
from app.services.issue_classifier import classify_issue

nlp = spacy.load("en_core_web_sm")

KNOWN_PLACES = ["Udupi", "Kundapura", "bus stand", "temple", "highway"]

def analyze_text(text: str):
    doc = nlp(text)

    entities = [(ent.text, ent.label_) for ent in doc.ents]

    for place in KNOWN_PLACES:
        if place.lower() in text.lower():
            entities.append((place, "RULE_LOC"))

    sentiment = TextBlob(text).sentiment.polarity
    issue = classify_issue(text)

    return {
        "entities": list(set(entities)),
        "sentiment": sentiment,
        "issue": issue
    }
