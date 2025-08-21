"""
test_functionality.py
Test script for sentiment analysis functionality with interactive mode
"""

from analysis import analyze_text, multi_class_classification
from explanation import extract_keywords, explain_classification
from comparison import compare_sentiment
import numpy as np

def test_all_functions():
    # Test data
    texts = [
        "I love this product! It's amazing!",
        "This is terrible. I hate it.",
        "The weather is okay today."
    ]
    
    print("=== Testing analyze_text ===")
    for text in texts:
        result = analyze_text(text)
        print(f"'{text}' → {result['sentiment']} ({result['confidence']:.3f})")
    
    print("\n=== Testing multi_class_classification ===")
    result = multi_class_classification(texts[0])
    print(f"Text: '{result['text']}'")
    print(f"Classification: {result['classification']}")
    print(f"Confidence Distribution: {result['confidence_scores']}")
    
    print("\n=== Testing extract_keywords ===")
    keywords = extract_keywords(texts[0])
    print(f"Keywords from '{texts[0]}': {keywords}")
    
    print("\n=== Testing explain_classification ===")
    explanation = explain_classification(texts[1])
    print(f"Explanation: {explanation['explanation']}")
    
    print("\n=== Testing compare_sentiment ===")
    comparison = compare_sentiment(texts)
    print(f"Summary: {comparison['summary']}")
    print(f"Total texts: {comparison['total_texts']}")

def interactive_analysis():
    while True:
        text = input("\nEnter text to analyze (or 'quit' to exit): ")
        if text.lower() == 'quit':
            break
            
        # Basic sentiment
        basic = analyze_text(text)
        print("\n=== Basic Sentiment Analysis ===")
        print(f"Overall Sentiment: {basic['sentiment']}")
        print(f"Confidence Score: {basic['confidence']:.3f}")
        
        # Detailed classification
        multi = multi_class_classification(text)
        print("\n=== Detailed Sentiment Distribution ===")
        for label, score in multi['confidence_scores'].items():
            print(f"{label.capitalize()}: {score:.2f}%")
        
        # Keywords and explanation
        explain = explain_classification(text)
        print("\n=== Detailed Analysis ===")
        print(f"Key sentiment words: {', '.join(explain['keywords'])}")
        print(f"Analysis explanation: {explain['explanation']}")

if __name__ == "__main__":
    choice = input("Select mode (1 for test suite, 2 for interactive analysis): ")
    if choice == "1":
        test_all_functions()
    elif choice == "2":
        print("\nSentiment Analysis Interactive Mode")
        print("----------------------------------")
        interactive_analysis()
    else:
        print("Invalid choice. Exiting.")