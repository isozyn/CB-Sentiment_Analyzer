"""
test_functionality.py
Test script for sentiment analysis functionality with interactive mode
"""

from analysis import analyze_text, multi_class_classification
from explanation import extract_keywords, explain_classification
from comparison import compare_sentiment
import numpy as np


# 🔹 Unified function: analyze a single string with all tools
def analyze_user_input(user_text: str):
    print("\n---------------------------------")
    print(f"User Input: '{user_text}'")

    # 1. Sentiment analysis
    sentiment_result = analyze_text(user_text)
    print(f"[Sentiment Analysis] → {sentiment_result['sentiment']} "
          f"(Confidence: {sentiment_result['confidence']:.3f})")

    # 2. Multi-class classification
    classification = multi_class_classification(user_text)
    print(f"[Classification] → {classification['classification']}")
    print(f"[Classification Scores] → {classification['confidence_scores']}")

    # 3. Keyword extraction
    keywords = extract_keywords(user_text)
    print(f"[Keywords] → {keywords}")

    # 4. Explanation
    explanation = explain_classification(user_text)
    print(f"[Explanation] → {explanation['explanation']}")

    return {
        "sentiment": sentiment_result,
        "classification": classification,
        "keywords": keywords,
        "explanation": explanation
    }


# 🔹 Test multiple strings in sections
def test_user_input_analysis():
    test_strings = [
        "I absolutely adore this game, it’s so fun!",
        "This food is disgusting, I’m never coming back.",
        "It’s an average day, nothing special."
    ]

    results = []
    for text in test_strings:
        result = analyze_user_input(text)
        results.append(result)

    return results


# 🔹 Compare sentiment across all test strings
def test_comparison_on_all():
    texts = [
        "I absolutely adore this game, it’s so fun!",
        "This food is disgusting, I’m never coming back.",
        "It’s an average day, nothing special."
    ]

    print("\n=== Overall Sentiment Comparison ===")
    comparison = compare_sentiment(texts)
    print(f"Summary: {comparison['summary']}")
    print(f"Total texts: {comparison['total_texts']}")


if __name__ == "__main__":
    # Run per-string section analysis
    test_user_input_analysis()

    # Run overall comparison
    test_comparison_on_all()
