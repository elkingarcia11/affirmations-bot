import csv_utils
import image_utils
import gcs_utils
import datetime
import random
from twitter_client import TwitterClient

def tweet_random_line_from_csv():
    # File paths
    FILE_PATHS = {
        "font": "PlayfairDisplay.ttf"
    }

    # Get bucket from GCS
    bucket = gcs_utils.get_gcs_bucket("affirmations-bot")

    # Get blobs from GCS Bucket
    blobs = gcs_utils.get_blobs_from(bucket, FILE_PATHS)

    # List of affirmations for twitter captions
    CAPTIONS = [
        ("Affirm this energy today", "✨"),
        ("Claim it now", "✨"),
        ("Type 'YES' if this resonates with you", "✨"),
        ("Repeat after me", "✨"),
        ("Say", "🌟"),
        ("Believe", "🔥"),
        ("Tell the universe", "🌌"),
        ("Affirm and visualize", "💫"),
        ("Affirm", "💫"),
        ("Visualize", "💫"),
        ("Visualize it. Feel it. Attract it", "💫"),
        ("Dream it, believe it, achieve it", "💫")
    ]


    try:
        # Get current UTC time
        current_utc_time = datetime.datetime.now(datetime.timezone.utc)

        # Extract the current hour
        current_hour_utc = current_utc_time.hour

        twitter_client = TwitterClient()

        # Get text for the image
        tweet_text = csv_utils.get_random_text_from_csv("assets/affirmations.csv")
        if current_hour_utc % 2 == 0:

            # Generate image
            try:
                image = image_utils.generate_image(tweet_text, blobs[0])
                image_utils.add_image_to(image, "/tmp/")
            except Exception as e:
                print(f"Error generating image: {e}")
                return
            caption = random.choice(CAPTIONS)
            tweet = caption[0]
            twitter_client.post_tweet(tweet, "/tmp/image.jpg")
        else:
            caption = random.choice(CAPTIONS)
            tweet = f'{tweet_text} {caption[1]}'
            twitter_client.post_tweet(tweet)
    except Exception as e:
        print(f"An unexpected error occurred while tweeting affirmation: {e}")
