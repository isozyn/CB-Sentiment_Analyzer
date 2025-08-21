"""
analysis.py
Core sentiment analysis module using VADER and NumPy
"""

import numpy as np
from typing import Dict, Union, Optional
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize VADER analyzer
analyzer = SentimentIntensityAnalyzer()

def analyze_text(text: str) -> Dict[str, Union[str, float, dict]]:
    """
    Analyze sentiment of input text using VADER and NumPy processing.
    
    Args:
        text (str): Input text for sentiment analysis
        
    Returns:
        dict: Sentiment analysis results including sentiment classification,
              confidence scores, and detailed metrics
    """
    if not isinstance(text, str) or not text.strip():
        return {
            "text": text,
            "sentiment": "neutral",
            "confidence": 0.0,
            "detailed_scores": {
                "positive": 0.0,
                "neutral": 100.0,
                "negative": 0.0,
                "compound": 0.0
            }
        }

    # Get VADER scores
    scores = analyzer.polarity_scores(text)
    
    # Convert to numpy arrays for efficient processing
    scores_array = np.array([scores['pos'], scores['neu'], scores['neg']])
    normalized = np.round((scores_array / np.sum(scores_array)) * 100, 2)
    
    # Determine sentiment using numpy thresholds
    sentiment = np.select(
        [scores['compound'] >= 0.05, scores['compound'] <= -0.05],
        ['positive', 'negative'],
        default='neutral'
    )
    
    return {
        "text": text,
        "sentiment": sentiment,
        "confidence": abs(scores['compound']),
        "detailed_scores": {
            "positive": normalized[0],
            "neutral": normalized[1],
            "negative": normalized[2],
            "compound": scores['compound']
        }
    }

def multi_class_classification(text: str) -> Dict[str, Union[str, dict]]:
    """
    Perform multi-class sentiment classification.
    
    Args:
        text (str): Input text for classification
        
    Returns:
        dict: Classification results with confidence scores
    """
    if not isinstance(text, str) or not text.strip():
        return {
            "text": text,
            "classification": "neutral",
            "confidence_scores": {
                "positive": 33.33,
                "neutral": 33.34,
                "negative": 33.33
            }
        }

    # Get VADER scores
    scores = analyzer.polarity_scores(text)
    
    # Process scores with numpy
    score_array = np.array([scores['pos'], scores['neu'], scores['neg']])
    normalized = np.round((score_array / np.sum(score_array)) * 100, 2)
    
    # Create confidence scores
    confidence_scores = {
        "positive": float(normalized[0]),
        "neutral": float(normalized[1]),
        "negative": float(normalized[2])
    }
    
    # Determine classification
    classifications = np.array(['positive', 'neutral', 'negative'])
    classification = classifications[np.argmax(normalized)]
    
    return {
        "text": text,
        "classification": classification,
        "confidence_scores": confidence_scores
    }

def get_sentiment_metrics(text: str) -> Dict[str, float]:
    """
    Calculate additional sentiment metrics using NumPy.
    
    Args:
        text (str): Input text for analysis
        
    Returns:
        dict: Statistical metrics of sentiment analysis
    """
    scores = analyzer.polarity_scores(text)
    metrics = np.array([scores['pos'], scores['neu'], scores['neg']])
    
    return {
        "mean": float(np.mean(metrics)),
        "std": float(np.std(metrics)),
        "variance": float(np.var(metrics)),
        "max_score": float(np.max(metrics)),
        "min_score": float(np.min(metrics)),
        "compound": float(scores['compound'])
    }