from twython import Twython
from pymongo import *

conn = Connection('localhost')
db = conn.nosqltweets
twitter = Twython()

types = ['mongodb', 'cassandra', 'couchdb']

for db in types:
	print db
	search_results = twitter.searchTwitter(q="%s", rpp="100") % (db)
	for tweet in search_results["results"]:
		col = "db.(db) "
		from_user = tweet['from_user'].encode('utf-8')
		text = tweet['text']
		created_at = tweet['created_at']
		id_str = tweet['id_str']
		post = { 'id_str': id_str, 'from_user': from_user, 'created_at': created_at, 'text': text } 
		#col.insert(post) 
		print post
