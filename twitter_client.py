import os
import tweepy
from dotenv import load_dotenv
import tempfile

class TwitterClient:
    def __init__(self):
        """
        Initialize the Twitter client.

        Load necessary environment variables for authentication.
        """
        load_dotenv()  # Loading environment variables
        self.CONSUMER_KEY = os.getenv('TWITTER_CONSUMER_KEY')
        self.CONSUMER_SECRET = os.getenv('TWITTER_CONSUMER_SECRET')
        self.ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
        self.ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        self.load_twitter_client()

    def load_twitter_client(self):
        """
        Load the Twitter client using environment variables.

        Returns:
            tweepy.Client: The Twitter client instance.

        Description:
            This method initializes and returns the tweepy client using environment variables.
            Note: wait_on_rate_limit sleeps future requests until rate limit is lifted.
        """
        try: 
            twitter_api = tweepy.OAuth1UserHandler(
                consumer_key=self.CONSUMER_KEY,
                consumer_secret=self.CONSUMER_SECRET,
                access_token=self.ACCESS_TOKEN,
                access_token_secret=self.ACCESS_TOKEN_SECRET
            )

            client = tweepy.Client(
                consumer_key=self.CONSUMER_KEY,
                consumer_secret=self.CONSUMER_SECRET,
                access_token=self.ACCESS_TOKEN,
                access_token_secret=self.ACCESS_TOKEN_SECRET,
                wait_on_rate_limit=True
            )

            self.client_v1 = tweepy.API(twitter_api)
            self.client_v2 = client
        except Exception as e:
            print("An unexpected error occurred with v1:", e)

    def post_tweet(self, text, image_path=None):
        """
        Post the provided text to Twitter.

        Args:
            text (str): The text to be posted to Twitter.
            image_path (str or PIL Image, optional): Path to the image or PIL Image object.

        Returns:
            None

        Description:
            This method creates a tweet on Twitter using the provided text and optionally an image.
        """
        try:
            temp_file = None  # Initialize temp file variable
            if image_path:
                # Handle case where image_path is a PIL Image
                if hasattr(image_path, "save"):  # Check if it's an image object
                    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
                    image_path.save(temp_file.name)
                    temp_file.close()
                    image_path = temp_file.name  # Use the temporary file path
                
                # Ensure the file exists
                if not os.path.isfile(image_path):
                    raise FileNotFoundError(f"Image file not found: {image_path}")
                
                # Upload media using v1 API
                media = self.client_v1.media_upload(filename=image_path)
                media_id = media.media_id
                print(f"Uploaded media ID: {media_id}")
                
                # Post tweet with image using v2 API
                self.client_v2.create_tweet(
                    text=text,
                    media_ids=[media_id]
                )
            else:
                # Post tweet without image
                self.client_v2.create_tweet(text=text)
            
            print(f"Tweeted: {text}")
        except tweepy.TweepyException as e:
            print(f"Tweepy Exception: {e}")
        except FileNotFoundError as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred posting tweet: {e}")