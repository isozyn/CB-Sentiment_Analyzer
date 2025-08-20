from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze(self, text: str) -> dict:
        """
        Analyze sentiment and return both scores and label.
        """
        score = self.analyzer.polarity_scores(text)

        # Determine sentiment label
        if score['compound'] >= 0.05:
            label = "positive"
        elif score['compound'] <= -0.05:
            label = "negative"
        else:
            label = "neutral"

        return {
            "text": text,
            "label": label,
            "scores": score
        }
if __name__ == "__main__":
    analyzer = SentimentAnalyzer()
    print(analyzer.analyze("I love programming!"))