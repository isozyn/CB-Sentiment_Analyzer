"""
Sentiment Analysis Package
"""

from analysis import analyze_text, multi_class_classification
from explanation import extract_keywords, explain_classification
from comparison import compare_sentiment

__all__ = [
    'analyze_text',
    'multi_class_classification', 
    'extract_keywords',
    'explain_classification',
    'compare_sentiment'
]