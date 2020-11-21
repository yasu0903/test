#https://qiita.com/cedric-ryo/items/17fdfec15ff88d877a4c
from requests_oauthlib import OAuth1Session
import json,config,datetime,pytz # import from library and config.py

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS) #auth

url = "https://api.twitter.com/1.1/statuses/home_timeline.json"

params = {"count": 50}
req = twitter.get(url, params = params)

if req.status_code == 200:
	timeline = json.loads(req.text)
	for tweet in timeline:
		print(tweet[u'user'][u'name'],"@",tweet[u'user'][u'screen_name'],tweet['created_at'])
		print(tweet[u'text'])
		print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
else:
	print ("Error: %d" % req.status_code)
