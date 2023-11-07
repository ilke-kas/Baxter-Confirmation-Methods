# Import necessary libraries

from fer import FER
from fer import Video
import pandas as pd
# Define pre-trained emotion detector

emotion_detector = FER(mtcnn=True)
# Define the path to video

path_to_video = "p4_no.mp4"

# Define video 

video = Video(path_to_video)
# Analyze the video and display the output

result = video.analyze(emotion_detector, display=True)
# Create Pandas DataFrame with emotion data

emotions_df = video.to_pandas(result)
emotions_df.head()
# Predict whether a person show interest in a topic or not
print(emotions_df)
# Function to find the dominant emotion
def find_dominant_emotion(row):
    emotions = [ "fear", "happy", "sad", "surprise", "neutral"]
    max_emotion = max(emotions, key=lambda emotion: row[emotion])
    return max_emotion

# Apply the function to create the "dominant_emotion" column
emotions_df["dominant_emotion"] = emotions_df.apply(find_dominant_emotion, axis=1)

# Print the updated DataFrame
print(emotions_df)
most_common_emotion = emotions_df["dominant_emotion"].mode()[0]

print(f"The most common emotion is: {most_common_emotion}")