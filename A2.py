import tweepy
from ClientKeys import *

# Override tweepy.StreamListener to add logic to on_status

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)
        responseT = status.text
        tweetparts(responseT)

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False


def tweetparts(response):
    part2 = response.split(" ", 2)[1]
    command = part2.split(":")[0]
    part22 = part2.split(":")[1]
    place = part22.split("+")[0]
    subject = part2.split("+")[1]
    if command == "p":
        message = response.split(" ", 2)[2]
        print(message)
    print(command)
    print(place)
    print(subject)



# Consumer Keys
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)
# api.update_status('tweepy + oauth!')

# Stream
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
hashtag = '#ECE4564T09'
response = myStream.filter(track=[hashtag], is_async=True)


# example response #ECE4564T18 p:Squires+Wishes “I wish I had gotten their number.”

