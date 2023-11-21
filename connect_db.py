import psycopg2
from fer import FER
from fer import Video
import pandas as pd
import sys

def insert_row(cursor, new_row_data):
    insert_query = """
    INSERT INTO emotion_recognition (userid, visual, verbal, body, no_confirm)
    VALUES (%(userid)s, %(visual)s, %(verbal)s, %(body)s, %(no_confirm)s);
    """

    # Execute the query with the data
    cursor.execute(insert_query, new_row_data)

    # Commit the changes to the database
    connection.commit()
    print("Row inserted successfully.")

def remove_row(cursor, userid):
    # Construct and execute the DELETE query
    delete_query = """
    DELETE FROM emotion_recognition
    WHERE userid = %(userid)s;
    """

    cursor.execute(delete_query, {'userid': userid})

    # Commit the transaction
    connection.commit()

    print(f"Row with userid {userid} deleted successfully.")

def process_video(participant_name, confirmation_method):
    # Emotion detection part
    # Define pre-trained emotion detector
    emotion_detector = FER(mtcnn=True)
    # Define the path to video
    path_to_video = ".\\videos\\"+ participant_name + "_" + confirmation_method + ".mp4"
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
    
    print(f"The most common emotion is: {most_common_emotion} for {confirmation_method}")
    return most_common_emotion
if len(sys.argv) > 1:
    # Access command line arguments starting from index 1
    # (index 0 is the script name itself)
    arg1 = sys.argv[1]
    
    print("Argument 1:", arg1)
    # Connection parameters
    db_params = {
        'host': 'localhost',     # Change this if your database is on a different host
        'port': '5432',          # Default PostgreSQL port
        'database': 'baxter',    # Your database name
        'user': 'postgres', # Your database username
        'password': '1515'  # Your database password
    }

    try:
        participant_name = arg1
        # Establish a connection to the database
        connection = psycopg2.connect(**db_params)
        new_data = {'userid':participant_name}
        # Create a cursor object to interact with the database
        cursor = connection.cursor()
        confirmation_methods = ["visual","verbal","body","no_confirm"]
        for conf_method in confirmation_methods:
            most_common_emotion = process_video(participant_name, conf_method)
            new_data[conf_method] = most_common_emotion 
        insert_row(cursor, new_data)

    except (Exception, psycopg2.Error) as error:
        print(f"Error: {error}")

    finally:
        # Close the cursor and connection
        if connection:
            cursor.close()
            connection.close()
            print("Connection closed.")


else:
    print("No command line arguments provided.")

