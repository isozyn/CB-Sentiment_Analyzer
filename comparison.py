"""
comparison.py
Multi-text sentiment comparison functions
"""

from analysis import analyze_text

def compare_sentiment(texts: list[str]) -> dict:
    """Compare sentiment across multiple texts"""
    if not texts:
        return {"results": [], "summary": {"positive": 0, "neutral": 0, "negative": 0}}
    
    results = []
    counts = {"positive": 0, "neutral": 0, "negative": 0}
    
    for text in texts:
        result = analyze_text(text)
        results.append(result)
        counts[result["sentiment"]] += 1
    
    # Calculate percentages
    total = len(texts)
    summary = {
        "positive": round((counts["positive"] / total) * 100),
        "neutral": round((counts["neutral"] / total) * 100), 
        "negative": round((counts["negative"] / total) * 100)
    }
    
    return {
        "results": results,
        "summary": summary,
        "total_texts": total
    }