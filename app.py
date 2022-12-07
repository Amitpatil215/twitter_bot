# Importing Tweepy
import tweepy

# Credentials
api_key = "XbRmXoayGrQhHq84QDVZm0KO6"
api_secret = "1fOMxG3SbmJIaQQF74TCY8G7XXHNSgAm13uvAlcKLD8h2lzEPn"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAM1zkAEAAAAAH9YUKhXpB21Tpg9GXobnLqn7a10%3DrQLz6ZB9h71qVFdULkXgim2NhoqkWzDLaGYVwUZtQtXxTAl6gZ"
access_token = "1021021522817835008-TZbbUmzVM5rQzcbYslg8SdwW1ivpMm"
access_token_secret = "BoNnPDakN8RjGGnIUHL9emkALGKTJqgYmIt05oQaGRlSL"

# Gainaing access and connecting to Twitter API using Credentials
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

# Creating API instance. This is so we still have access to Twitter API V1 features
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Creating a tweet to test the bot
client.create_tweet(text="Hello World")