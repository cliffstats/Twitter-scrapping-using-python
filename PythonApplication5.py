
##Consumer Key (API Key)	xDl9q32JAlweCiptXYcbAJiin
##Consumer Secret (API Secret)	UxZjQF7KRLODOtX59QMfXYwFbhBIYzY0aXZt9hWjMaJ05O0yRT
##Access Level	Read and write (modify app permissions)
##Owner	vdj_cliffo
##Owner ID	4032831017
##Access Token	4032831017-AKJPIatZxvNb4Krhlj4DmcfXGmaNDNqGss6vsyB
##Access Token Secret	iykrK09v7kIy7gmdRe4J2xO7PNUGLM5EENS1s5nmNhCWi


import tweepy
from textblob import TextBlob

consumer_key = "xDl9q32JAlweCiptXYcbAJiin"
consumer_secret = "UxZjQF7KRLODOtX59QMfXYwFbhBIYzY0aXZt9hWjMaJ05O0yRT"
access_token = "4032831017-AKJPIatZxvNb4Krhlj4DmcfXGmaNDNqGss6vsyB"
access_token_secret = "iykrK09v7kIy7gmdRe4J2xO7PNUGLM5EENS1s5nmNhCWi"

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

