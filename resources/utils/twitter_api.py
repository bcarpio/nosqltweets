import tweepy
from pprint import pprint

consumer_key="9qtL4OHj9aZpFCWO2TAeig"
consumer_secret="PXggjnvMb89sRc0Jp70LvSjYO4zpBv3dKJ2X1bD2Q"

access_token="12545732-6KF0EzUOKrCUvM4Cyi4oLsagVD3OomvDyK8yP2HVs"
access_token_secret="ufLU2L7F0cQlm0HwE6fQ55B1CV8NiGDab8UMlm1rnI"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

print api.me().name
for saved in api.saved_searches():
	pprint(saved) 
