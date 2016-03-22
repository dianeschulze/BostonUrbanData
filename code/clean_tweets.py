import csv, re, string
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

# print(re.sub('((http:\/\/)|(https:\/\/))?\S+\.\S+\.\S+\/?\S*', '', "Every1 knows of it, but does anyone know who actually owns it? Can't find such info anywhere.. @CityOfBoston @BOS311 pic.twitter.com/RIuu9J66cS"))
# 1. Get a lot of tweets (check)
# ==> Used a Github Library to access old tweets.

tweets_csv = "data/got_people_tweets.csv"
tweet_texts = []
punctuation = set(string.punctuation)
stop_words = stopwords.words("english")
with open(tweets_csv, 'r') as f:
	tw_reader = csv.reader(f, delimiter=';')
	# next(tw_reader, None)
	for row in tw_reader:
		text = row[4]
# 2. Clean words 
#   a) remove links
		print('ORIGINAL:: ' + text)
		text = re.sub('(https?:\/{2}( |\S+)?)?(\S*\.?\S+\.\S+\/?\S*)?(\S+\/\S+)', '', text)
#	b) remove usernames
		text = re.sub('@\S+','', text)
#	d) remove punctuation (includes hashtags)
		text = ''.join(ch for ch in text if ch not in punctuation)
# 	e) lowercase
		text = text.lower()
#	i) remove multiple whitespace and strip
		text = re.sub('\s+', ' ', text).strip()
# 	g) remove stopwords 
		text = ' '.join([word for word in text.split() if word not in stop_words])
		print('PROCESSED:: ' + text)
# 	f) combines word stems (plural vs singular, verb conjugation, etc..) 
#	h) remove repetition (RT issues)
#	? remove strings with both digits and letters


# 3. Word cloud



# Types of problems
