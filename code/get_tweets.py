import tweepy, json, datetime, time, csv, re, stemming
from tweepy import OAuthHandler
from twitter_access import *

# auth = OAuthHandler(consumer_key, consumer_secret)
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

if (not api):
	print("Failed to Authenticate")
	sys.exit(-1)

# TODO: remove cases where there are two links (greedy makes location include a url link

# City of boston tweets
# with open('city_of_boston_tweets.csv', 'w') as f:
# 	tweet_writer = csv.writer(f)
# 	tweet_writer.writerow(['case_status', 'location','date', 'text']);
# 	for status in tweepy.Cursor(api.user_timeline, screen_name='BOS311x').items(320):
# 		if (datetime.datetime.now() - status.created_at).days < 7:
# 			text = status.text
# 			case_status = text.split()[0]
# 			text_search = re.search('at (.*) https', text)
# 			location = ""
# 			date = status.created_at.strftime("%Y-%m-%d %H:%M:%S")
# 			if text_search:
# 				location = text_search.group(1)
# 			tweet_writer.writerow([case_status.encode('utf-8'), location.encode('utf-8'), date.encode('utf-8'), text.encode('utf-8')])
# 		else:
# 			break;

######### People tweets ##############################

# searchQuery = '@BOS311'  # this is what we're searching for
# maxTweets = 1000 # Some arbitrary large number
# tweetsPerQry = 100  # this is the max the API permits
fName = 'people_tweets.csv' # We'll store the tweets in a text file.


# # If results from a specific ID onwards are reqd, set since_id to that ID.
# # else default to no lower limit, go as far back as API allows
# sinceId = None

# # If results only below a specific ID are, set max_id to that ID.
# # else default to no upper limit, start from the most recent tweet matching the search query.
# max_id = -1L

# tweetCount = 0
# print("Downloading max {0} tweets".format(maxTweets))

with open(fName, 'w') as f:
	tweet_writer = csv.writer(f)
	# tweet_writer.writerow(['location', 'date', 'text']) #add location using ('(/d .* ave|st')
	tweet_writer.writerow(['date', 'text'])
# 	while tweetCount < maxTweets:
# 		try:
# 			# Pagination
# 			if (max_id <= 0):
# 				if (not sinceId):
# 					new_tweets = api.search(q=searchQuery, count=tweetsPerQry)
# 				else:
# 					new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
# 											since_id=sinceId)
# 			else:
# 				if (not sinceId):
# 					new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
# 											max_id=str(max_id - 1))
# 				else:
# 					new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
# 											max_id=str(max_id - 1),
# 											since_id=sinceId)

# 			# New Tweets
# 			if not new_tweets:
# 				print("No more tweets found")
# 				break
# 			for tweet in new_tweets:
		
# 				print(tweet.created_at.strftime("%Y-%m-%d %H:%M:%S") + ", " + tweet.text.encode('utf-8'))
# 				tweet_writer.writerow([tweet.created_at.strftime("%Y-%m-%d %H:%M:%S"), tweet.text.encode('utf-8')])

# 			tweetCount += len(new_tweets)
# 			print("Downloaded {0} tweets".format(tweetCount))
# 			max_id = new_tweets[-1].id

# 		except tweepy.TweepError as e:
# 				# Just exit if any error
# 				print("some error : " + str(e))
# 				break

# print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))

	# for status in tweepy.Cursor(api.search, q="@BOS311", geocode="42.3583333,-71.0602778,10mi").items(10):
	tweet_texts = []
	c1 = 0;
	for tweet in tweepy.Cursor(api.search, q="@BOS311", count=1).items(100):
		# text_search = re.search('((\d+ )?\w+ (ave|st)) ', tweet.text, re.IGNORECASE)
		# location = ""
		# if text_search:
		# 	location = text_search.group(1)
		# tweet_writer.writerow([location, tweet.created_at.strftime("%Y-%m-%d %H:%M:%S"), tweet.text.encode('utf-8')])
		c1 += 1
		# c2 = 0
		# for tweet in page:
			# print(len(page))
			# c2 += 1
		print(str(c1))
		time = tweet.created_at.strftime("%Y-%m-%d %H:%M:%S")
		text = tweet.text.encode('utf-8')
		rt_search = re.search('RT @[\w\d]+:(.*)', text) # get text of tweet that was retweeted
		if rt_search:
			text = rt_search.group(1).strip();
		if text not in tweet_texts: # eliminate duplicates (because of retweets)
			tweet_texts.append(text)
			# print( + ", " + )
			tweet_writer.writerow([time, text])
		# if (datetime.datetime.now() - tweet.created_at).days < 7:
		# 	tweet_writer.writerow([tweet.text.encode('utf-8')])
		# else:
		# 	break

with open('results.txt', 'w') as f:
	for tweet in tweepy.Cursor(api.search, q="@BOS311").items(10):
		# print(tweet.retweeted)
		# if (tweet.retweeted):
			f.write(str(tweet));
			# break;

# 1. get a lot of tweets
# 2. word cloud 
	# lowercase
	# combines word stems
	# remove stopwords



# Types of problems

