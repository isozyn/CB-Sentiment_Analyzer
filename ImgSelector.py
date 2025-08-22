def Select_image(sentiment):
    """
    Select appropriate emoji based on sentiment.
    
    Args:
        sentiment (str): The sentiment ('positive', 'negative', 'neutral')
        
    Returns:
        str: Emoji character representing the sentiment
    """
    # Define the mapping of sentiments to emojis
    emoji_mapping = {
        'positive': '😊',
        'negative': '😢', 
        'neutral': '😐'
    }
    
    # Default to neutral if sentiment not recognized
    sentiment = sentiment.lower()
    return emoji_mapping.get(sentiment, '😐')