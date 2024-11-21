import os
import tweepy
from dotenv import load_dotenv

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
        self.client_v2 = self.load_twitter_client()

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
            auth = tweepy.OAuth1UserHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
            auth.set_access_token(
                self.ACCESS_TOKEN,
                self.ACCESS_TOKEN_SECRET,
            )
            self.client_v1 = tweepy.API(auth)
        except Exception as e:
            print("An unexpected error occurred with v1:", e)

        try:
            client = tweepy.Client(
                consumer_key=self.CONSUMER_KEY,
                consumer_secret=self.CONSUMER_SECRET,
                access_token=self.ACCESS_TOKEN,
                access_token_secret=self.ACCESS_TOKEN_SECRET,
                wait_on_rate_limit=True
            )

            return client
        except tweepy.TweepyException as e:
            print("Tweepy Exception:", e)
        except Exception as e:
            print("An unexpected error occurred with v2:", e)
        return None

    def post_tweet(self, text, image_path=None):
        """
        Post the provided text to Twitter.

        Args:
            text (str): The text to be posted to Twitter.

        Returns:
            None

        Description:
            This method creates a tweet on Twitter using the provided text.
        """
        try:
            if image_path:
                media = self.client_v1.media_upload(filename=image_path)
                media_id = media.media_id

                # Create a tweet with text and the uploaded image
                self.client_v2.create_tweet(
                    text=text,
                    media_ids=[media_id]
                )
            else:
                self.client_v2.create_tweet(text=text)
            print(f"Tweeted: {text}")
        except tweepy.TweepyException as e:
            print("Tweepy Exception:", e)
        except Exception as e:
            print("An unexpected error occurred posting tweet:", e)