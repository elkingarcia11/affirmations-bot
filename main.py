import csv_utils
import image_utils
import gcs_utils
import datetime
import random
from twitter_client import TwitterClient

def tweet_random_line_from_csv():
    # File paths
    FILE_PATHS = [
        "affirmations-bot",
        "assets/affirmations.csv",
        "PlayfairDisplay.ttf",
        "dark.png",
        "dark1.png",
        "dark2.png",
        "dark3.png",
        "dark5.png",
        "dark6.png",
        "dark7.png",
        "dark8.png",
        "dark10.png",
        "dark11.png",
    ]

    # List of affirmations for twitter captions
    CAPTIONS = [
        ("Affirm this energy today", "✨"),
        ("Claim it now", "✨"),
        ("Type 'YES' if this resonates with you", "✨"),
        ("Repeat after me", "✨"),
        ("Repost this to affirm", "🌟"),
        ("Like this to affirm", "🌟"),
        ("Believe", "💫"),
        ("Tell the universe", "🌌"),
        ("Affirm and visualize", "🙏"),
        ("Affirm", "🙏"),
        ("Visualize", "🙏"),
        ("Visualize it. Feel it. Attract it", "🧘"),
        ("Dream it, believe it, achieve it", "💫")
    ]

    try:
        # Get bucket from GCS
        bucket = gcs_utils.get_gcs_bucket(FILE_PATHS[0])

        # Initialize twitter client
        twitter_client = TwitterClient()

        # Get text for the image
        tweet_text = csv_utils.get_random_text_from_csv(FILE_PATHS[1])

        # Get font blob
        font_blob = gcs_utils.get_blob_from(bucket, FILE_PATHS[2])

        # Get current UTC time
        current_utc_time = datetime.datetime.now(datetime.timezone.utc)

        # Extract the current hour
        current_hour_utc = current_utc_time.hour

        remainder = current_hour_utc % 4

        if remainder == 0:
            # Generate image
            try:
                image = image_utils.generate_image_from_colors(tweet_text, font_blob)
                image_path = "/tmp/image.jpg"
                image.save(image_path)
            except Exception as e:
                print(f"Error generating image: {e}")
                return
            caption = random.choice(CAPTIONS)
            tweet = caption[0]
            twitter_client.post_tweet(tweet, "/tmp/image.jpg")
        elif remainder == 2:
            # Generate image
            try:
                image_file = random.choice(FILE_PATHS[3:])
                image_blob = gcs_utils.get_blob_from(bucket, image_file)
                image = image_utils.generate_image_from_blob(image_blob, tweet_text, font_blob)
                image_path = "/tmp/image.jpg"
                image = image.convert("RGB")
                image.save(image_path, "JPEG")
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
        print(f"Error generating image from colors: {e}, Tweet text: {tweet_text}")
   
tweet_random_line_from_csv()