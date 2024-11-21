import csv
import random
import date_utils
import csv_utils
import image_utils
import datetime
from twitter_client import TwitterClient

def tweet_random_line_from_csv():
    # Get the current UTC time 
    now = datetime.datetime.now(datetime.timezone.utc)

    sub_ranges = date_utils.define_sub_ranges(now)
    sub_range_index = date_utils.check_sub_ranges(now, sub_ranges)
    text = csv_utils.get_random_text_from_csv("assets/affirmations.csv")
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
    text, import_filepath, state, output_filepath = "","","", "assets/image.jpg"

    if sub_range_index == 1:
        print("Current UTC time is between 12:00 PM and 5:59 PM UTC.")
        import_filepath = "assets/morning.jpg"
        state = "morning"
    elif sub_range_index == 2:
        print("Current UTC time is between 6:00 PM and 11:59 PM UTC.")
        import_filepath = "assets/evening.jpg"
        state = "evening"
    else:
        # sub_range_index == 3:
        print("Current UTC time is between 12:00 AM and 4:59 AM UTC.")
        import_filepath = "assets/night.jpg"
        state = "night"
    
    image = image_utils.draw_in_center(text, import_filepath, state)
    image_utils.add_image_to(image,"assets/image.jpg")
    try:
        twitter_client = TwitterClient()
        text = random.choice(affirmations)
        twitter_client.post_tweet(text[0], image)
    except Exception as e:
        print(f"An unexpected error occurred while processing news: {e}")

        

tweet_random_line_from_csv()