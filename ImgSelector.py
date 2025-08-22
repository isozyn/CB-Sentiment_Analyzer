import os

def Select_image(sentiment):
    if sentiment.lower() == "negative":
        return os.path.join("images", "negative.png")
    elif sentiment.lower() == "positive":
        return os.path.join("images", "positive.png")
    else:
        return os.path.join("images", "neutral.png")
