"""
explanation.py
Module for explaining sentiment analysis results
"""

import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def extract_keywords(text: str) -> list:
    """
    Extract keywords from text.
    
    Args:
        text (str): Input text
        
    Returns:
        list: List of keywords
    """
    # Simple keyword extraction - split and filter
    words = re.findall(r'\b\w+\b', text.lower())
    # Filter out common stop words
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'being'}
    keywords = [word for word in words if word not in stop_words and len(word) > 2]
    return keywords[:5]  # Return top 5 keywords

def explain_classification(text: str) -> dict:
    """
    Explain why the text was classified with a particular sentiment.
    
    Args:
        text (str): Input text for explanation
        
    Returns:
        dict: Explanation of the classification
    """
    if not isinstance(text, str) or not text.strip():
        return {
            "explanation": "No text provided for analysis.",
            "keywords": []
        }
    
    # Get VADER scores
    scores = analyzer.polarity_scores(text)
    
    # Extract keywords
    keywords = extract_keywords(text)
    
    # Determine sentiment
    if scores['compound'] >= 0.05:
        sentiment = 'positive'
    elif scores['compound'] <= -0.05:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    
    # Generate explanation based on sentiment and scores
    if sentiment == 'positive':
        explanation = f"This text was classified as positive because it contains positive language indicators. The compound score is {scores['compound']:.2f}, which indicates a positive sentiment."
    elif sentiment == 'negative':
        explanation = f"This text was classified as negative because it contains negative language indicators. The compound score is {scores['compound']:.2f}, which indicates a negative sentiment."
    else:
        explanation = f"This text was classified as neutral because it contains a balanced mix of positive and negative indicators, or lacks strong emotional language. The compound score is {scores['compound']:.2f}."
    
    if keywords:
        explanation += f" Key words contributing to this analysis include: {', '.join(keywords)}."
    
    return {
        "explanation": explanation,
        "keywords": keywords
    }