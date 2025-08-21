"""
explanation.py
Explanation and keyword extraction functions
"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from analysis import analyze_text
import re

analyzer = SentimentIntensityAnalyzer()

def extract_keywords(text: str) -> list[str]:
    """Extract sentiment-driving keywords from text"""
    if not text.strip():
        return []
    
    # Split into words and clean
    words = re.findall(r'\b\w+\b', text.lower())
    keywords = []
    
    for word in words:
        word_score = analyzer.polarity_scores(word)
        if abs(word_score["compound"]) > 0.1:  # Only significant sentiment words
            keywords.append(word)
    
    return keywords[:5]  # Return top 5 keywords

def explain_classification(text: str) -> dict:
    """Explain why text received its sentiment classification"""
    result = analyze_text(text)
    keywords = extract_keywords(text)
    
    if not keywords:
        explanation = f"Text classified as '{result['sentiment']}' with low confidence due to neutral language."
    else:
        keyword_str = ", ".join(keywords)
        explanation = f"Text classified as '{result['sentiment']}' based on key words: {keyword_str}"
    
    return {
        "text": text,
        "classification": result["sentiment"],
        "confidence": result["confidence"],
        "keywords": keywords,
        "explanation": explanation
    }