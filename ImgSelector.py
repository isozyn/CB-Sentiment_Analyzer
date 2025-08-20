def Select_image(sentiment):
    if sentiment == "positive":
        return("images/positive.png")
    elif sentiment == "negative":
        return("images/negative.png")
    elif sentiment == "neutral":
        return("images/neutral.png")
