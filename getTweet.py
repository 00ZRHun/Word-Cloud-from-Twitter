# tut url: https://sarvesh-amrute19.medium.com/how-to-extract-tweets-from-twitter-using-python-bcb37ce2be73
import pandas as pd   # make dataframe, export csv
import tweepy   # extract tweets from Twitter
text = 123
'''print("stats_folder_path:", text)
print("stats_folder_path: {}".format(text))'''
# print(f'text = {text}')

# import package

# set credentials
consumer_key = "q1BwFxmCRcLt21Wwx33zXqQVR"   # same as api key
# same as api secret
consumer_secret = "rjMIMoYhoOVg6K1wnFEi8vtMtn64hPZChHXDh8JxmcR0Sx9Myg"
access_key = "1267374302971617282-IB4B6Lfi1QxitPTzw4h5wRRxjjRI6a"
access_secret = "3iRqJsKLExVAj4tcUoQ0pw3yRAhpBEM1jpcWBvPLzGCfj"

# Twitter authentication
# - creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# - setting your access token and secret
auth.set_access_token(access_key, access_secret)

# creating an API
# - creating the API object while passing in auth information
api = tweepy.API(auth)

# extact tweets
# 1. username: for a particular user mention
# TRY: 'extended' -> "extended"
username_tweets = tweepy.Cursor(
    api.search_tweets, q="@elonmusk", tweet_mode='extended',
    lang="en"
).items(5+1)

# iterate over the tweets & print them one by one
for tweet in username_tweets:
    text = tweet._json["full_text"]
    # TODO: print for each item (not 1 only)
    # print(text)
    # print(f"text = {text}")
    print("text:", text)

    # using different attributes
    print("tweet.favorite_count:", tweet.favorite_count)
    print("tweet.retweet_count:", tweet.retweet_count)
    print("tweet.created_at:", tweet.created_at)

    # OR use List Comprehension to get all the tweets in a list
    # username_tweets_list = [tweet.text for tweet in username_tweets]
    username_tweets_list = [tweet._json["full_text"]
                            for tweet in username_tweets]
    print("username_tweets_list:", username_tweets_list)
    # printing the recent tweet mentioning elonmusk # use '//' for comment
    print("username_tweets_list[0]:", username_tweets_list[0])

# 2. hashtag: for a particular hashtag
hashtag_tweets = tweepy.Cursor(
    api.search_tweets, q="#VaccinationDrive", tweet_mode='extended').items(5)
print("\n=== hashtag_tweets ===")
for tweet in hashtag_tweets:
    text = tweet._json["full_text"]
    print("text:", text)

# 3. date filter: tweets after a mentioned date
date_tweets = tweepy.Cursor(
    api.search_tweets, q="@elonmusk", since="2020-5-31", tweet_mode='extended').items(5)
print("\n=== date_tweets ===")
for tweet in date_tweets:
    text = tweet._json["full_text"]
    print("text:", text)

# 4. particular user account: all tweets created by a particular user account since it's very first tweet
new_tweets = tweepy.Cursor(
    api.user_timeline, screen_name="elonmusk", tweet_mode='extended').items(10)
print("\n=== new_tweets ===")
for tweet in new_tweets:
    text = tweet._json["full_text"]
    print("text:", text)

# iterate through the new_tweets
print("\n=== new_tweets list ===")
list = []
print("IMPORTANT: new_tweets", new_tweets)
for tweet in new_tweets:
    text = tweet._json["full_text"]
    print("IMPORTANT: tweet:", tweet)
    print("IMPORTANT: tweet._json['id']:", tweet._json['id'])
    print("IMPORTANT: tweet._json['status']:", tweet._json['status'])

    refined_tweet = {'text': text,
                     'favorite_count': tweet.favorite_count,
                     'retweet_count': tweet.retweet_count,
                     'created_at': tweet.created_at}

    list.append(refined_tweet)
print("list:", list)

print("IMPORTANT: [tweet._json for tweet in new_tweets] = ",
      [tweet._json for tweet in new_tweets])

# make a dataframe of tweets with columns representing the different attributes of tweet
df = pd.DataFrame(list)
df.to_csv('refined_tweets.csv')
print("df", df)
