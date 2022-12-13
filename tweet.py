import tweepy
import time

auth = tweepy.OAuthHandler('Asp5miVjEjNk4fgELNgVLsYxY',
                           'IVt9AIt5uCoqJR48okj97vFVNI3WfPxGRFyl9e2w2aIRE49xCF')
auth.set_access_token('1602742738021220352-afIBXRDmjZys9UHXEuE5GXneENcJJN',
                      'UCkewMrMJXdC83nzYHV4BTE5zzq2lgTuWRap3VoeaSbXq')

api = tweepy.API(auth)
user = api.me()


# Helper function to ensure we don't overload the twitter server


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(500)

# Python loving bot likes tweet that mention python!


search_string = 'python'
numberOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        print('I liked the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break


# # Generous Bot follows back anyone that follows him!
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     follower.follow()
#     break

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
