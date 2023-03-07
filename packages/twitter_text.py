def get_tweets(keyword=None, hashtag=None):
    # import package
    import tweepy   # extract tweets from Twitter
    import pandas as pd   # make dataframe, export csv

    # set credentials
    consumer_key = "q1BwFxmCRcLt21Wwx33zXqQVR"   # same as api key
    # same as api secret
    consumer_secret = "rjMIMoYhoOVg6K1wnFEi8vtMtn64hPZChHXDh8JxmcR0Sx9Myg"
    access_key = "1267374302971617282-IB4B6Lfi1QxitPTzw4h5wRRxjjRI6a"
    access_secret = "3iRqJsKLExVAj4tcUoQ0pw3yRAhpBEM1jpcWBvPLzGCfj"

    # Twitter authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)

    # creating an API
    api = tweepy.API(auth)

    print("\n=== tweets ===")
    # query term
    if keyword is not None:
        query_term = keyword
    elif hashtag is not None:
        query_term = "#" + hashtag
    else:   # keyword is None & hashtag is None:
        query_term = "#VaccinationDrive"

    tweets = tweepy.Cursor(
        api.search_tweets, q=query_term, tweet_mode="extended").items(5)   # OPT: compat
    return tweets



def get_text(keyword=None, hashtag=None):
    tweets = get_tweets(keyword, hashtag)

    text = ""
    for tweet in tweets:
        print(f"IMPORTANT: tweet = {tweet}")
        text += tweet._json["full_text"]
        print("text:", text)
    
    # return text
    return text

def get_refined_tweet_list(keyword=None, hashtag=None):
    tweets = get_tweets(keyword, hashtag)
    
    refined_tweet_list = list()
    for tweet in tweets:
        print(f"IMPORTANT: tweet = {tweet}")
        text = tweet._json["full_text"]
        print("text:", text)

        refined_tweet = {'text': text,
                            'favorite_count': tweet.favorite_count,
                            'retweet_count': tweet.retweet_count,
                            'created_at': tweet.created_at}

        refined_tweet_list.append(refined_tweet)
        print("refined_tweet_list:", refined_tweet_list)

    # make a dataframe of tweets with columns representing the different attributes of tweet
    df = pd.DataFrame(refined_tweet_list)
    df.to_csv('refined_tweets.csv')
    print("df:", df)

    # return df
    return refined_tweet_list