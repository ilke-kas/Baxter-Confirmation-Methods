import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

data = {
    "Visual Confirmation": [
        "I have to point.OK. ",
        "Yes. Thank You.",
        "Yeah.",
        ""
    ],
    "Verbal Confirmation": [
        "",
        "Hello buddy. Oh. Yay. Yes.",
        "Yes, please.",
        ""
    ],
    "Body Movement for Confirmation": [
        "Oh, I should have said something. Okay, okay, Can we go back again?So I want the green cube. Yep, Yep. Go ahead and pick it up. Yep, yeah, that is the correct one. Pick it up. Thank you. Here faster did it. Yeah, very good. Yeah. Yeah, that good?",
        "",
        "",
        ""
    ],
    "No Confirmation": [
        "OK, can you pick the red cube?Red one. OK, pick it up. Yes. Yeah. That's it.",
        "Oh. Oh. Come on.",
        "Hello buddy. Oh. Yay. Yes. Yes. Hey, yeah, Sling.",
        ""
    ]
}
df = pd.DataFrame(data)
print(df)
# Define the sentiment analysis function using NLTK's SentimentIntensityAnalyzer
def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)
    
    if sentiment_scores['compound'] >= 0.05:
        return 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Apply sentiment analysis to the entire DataFrame
sentiment_df = df.applymap(analyze_sentiment)

print(sentiment_df)
