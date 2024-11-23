import csv_utils
import date_utils
import image_utils
import gcs_utils
import datetime
import random
from twitter_client import TwitterClient

def tweet_random_line_from_csv():
    # File paths
    file_paths = {
        "morning": "morning.jpg",
        "evening": "evening.jpg",
        "night": "night.jpg",
        "font": "PlayfairDisplay.ttf"
    }

    # Get bucket from GCS
    bucket = gcs_utils.get_gcs_bucket("affirmations-bot")

    # Get blobs from GCS Bucket
    blobs = gcs_utils.get_blobs_from(bucket, file_paths)

   
    # List of affirmations for twitter captions
    affirmations = [
        "Today is the perfect day to manifest greatness. 🕊️",
        "Claim this energy today. ✨",
        "Every day is a new opportunity to create your reality. 🌞",
        "Start now. The power is within you. 🌟",
        "Manifestation starts with belief. Keep going. 🌻",
        "Your thoughts are powerful. Keep them aligned with your dreams. 💭",
        "This is your reminder to dream big and trust yourself. 🌈",
        "Breathe in abundance, breathe out doubt. 🌬️💰",
        "You’re one step closer to your breakthrough. 🚀",
        "Believe it, feel it, and watch it unfold. 🌟",
        "Abundance is your birthright. Claim it now. 🌿",
        "What’s meant for you is already on its way. 💎",
        "Your time is coming—trust the process. ⏳",
        "Align your energy with your intentions, and miracles will happen. 🔮",
        "The universe is listening—speak your desires into existence. 🌌",
        "Type 'YES' if this resonates with you! 💫",
        "Repeat after me:",
        "Affirm and visualize:",
        "Visualize it. Feel it. Attract it. 💫",
        "The universe has your back. Always. 🌌",
        "Everything you desire is already aligned with your highest good. ✨",
        "Dream it, believe it, achieve it. The journey is yours. 🛤️",
        "This is your sign to keep manifesting. Magic is real. 🔥",
    ]

    # Get text for the image
    image_text = csv_utils.get_random_text_from_csv("assets/affirmations.csv")

    # Determine time of day
    now = datetime.datetime.now(datetime.timezone.utc)
    sub_ranges = date_utils.get_time_ranges(now)
    sub_range_index, state = date_utils.get_active_range_index(now, sub_ranges)

    if sub_range_index == 1:
        image_blob = blobs[0]
    elif sub_range_index == 2:
        image_blob = blobs[1]
    else:
        image_blob = blobs[2]

    # Generate image
    try:
        image = image_utils.draw_in_center(image_text, image_blob, state, blobs[3])
        image_utils.add_image_to(image, "/tmp/")
    except Exception as e:
        print(f"Error generating image: {e}")
        return

    # Post tweet
    try:
        twitter_client = TwitterClient()
        twitter_client.post_tweet(random.choice(affirmations), "/tmp/image.jpg")
    except Exception as e:
        print(f"An unexpected error occurred while tweeting affirmation: {e}")


tweet_random_line_from_csv()