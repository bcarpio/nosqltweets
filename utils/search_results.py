from twython import Twython
from pymongo import *
from datetime import *

conn = Connection('localhost')
db = conn.nosqltweets
twitter = Twython(
			twitter_token = '9qtL4OHj9aZpFCWO2TAeig',
			twitter_secret = 'PXggjnvMb89sRc0Jp70LvSjYO4zpBv3dKJ2X1bD2Q',
			oauth_token = '12545732-6KF0EzUOKrCUvM4Cyi4oLsagVD3OomvDyK8yP2HVs',
			oauth_token_secret = 'ufLU2L7F0cQlm0HwE6fQ55B1CV8NiGDab8UMlm1rnI',
	)

types = ['mongodb', 'cassandra', 'couchdb']

for nosql in types:
	search_results = twitter.searchTwitter(q='#%s'%(nosql), rpp="100")
	for tweet in search_results["results"]:
		collection = getattr(db, nosql)
		collection.ensure_index('id_str', unique=True)
		from_user = tweet['from_user'].encode('utf-8')
		text = tweet['text']
		created_at = datetime.strptime(tweet['created_at'], "%a, %d %b %Y %H:%M:%S +0000")
		id_str = tweet['id_str']
		post = { 'id_str': id_str, 'from_user': from_user, 'created_at': created_at } 
		collection.insert(post)
