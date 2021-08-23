import tweepy
from textblob import TextBlob

consumer_key = 'fok4Pu0OuWz4DTFQCB7SEl3Yt'

consumer_key_secret ='eziGfY2pKr3vUG8o1H6usXDj7j3GyYTJT6TLaW8oAZLYItUph5' 

access_token = '922446690216374272-SaHTiSeOgJE5bLR5eHwg4hUrQr0ftTN'

access_token_secret = 'ZqnqmEKlwc3ilWDbliCbN4uQMGg3MT6iCUb0E8cKuuV4S'







    
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Penguins')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	if analysis.sentiment[0]>0:
		print ('Positive')
	else:
		print ('Negative')
	print("")


