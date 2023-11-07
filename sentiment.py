import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

data = {
    "Visual Confirmation": [
        "I feel baxter should have stretched its hand further to me",
        "Didn't hand me my block :(",
        "I think the interaction was interesting overall, but felt a bit awkward as I wasn't sure when the robot would perform the task.",
        "I think the baxter’s arm should move faster"
    ],
    "Verbal Confirmation": [
        "I feel the cube shape should be improved",
        "Took away my block :(",
        "The voice verbal interaction component was interesting.",
        "This part has good interaction between the participant and baxter."
    ],
    "Body Movement for Confirmation": [
        "Baxter was excellent",
        "it worked!!",
        "I liked this component of the study as it was interesting to see if the robot could detect our verbal communication",
        "I love this way of confirmation, but confirmation part spend a lot of time which is not good enough"
    ],
    "No Confirmation": [
        "N/A",
        "It worked!!",
        "The robot handing the cube directly to me felt like a more personal interaction. DEF FELT a bit nervous and excited at the same time.",
        "It’s cool"
    ]
}

df = pd.DataFrame(data)

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
