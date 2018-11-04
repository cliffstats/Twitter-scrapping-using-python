import tweepy
from textblob import TextBlob

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

kenya_tweets = api.search("miguna")

fileName = "MigunaTweets.csv"
flo = open (fileName, "w")
headers = "Tweet, Polarity, Subjectivity\n"
flo.write(headers)

for tweet in kenya_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    #print(analysis.sentiment)
    print(analysis.sentiment.polarity)
    print(analysis.sentiment.subjectivity)
    #sentimentList = [analysis.sentiment]
    tweet = tweet.text
    flo.write(tweet.replace("," , " | ") + "," + str(analysis.sentiment.polarity) + "," + str(analysis.sentiment.subjectivity) + "\n")

flo.close()

