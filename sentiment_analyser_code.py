import re
import twitter_credentials
import twitter
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
import csv
from twitter import TwitterError
from twitter import TwitterError
#Initialise twitter API
twitter_api = twitter.Api(consumer_key=twitter_credentials.CONSUMER_KEY,

                          consumer_secret=twitter_credentials.CONSUMER_KEY_SECRET,
                          access_token_key=twitter_credentials.ACCESS_TOKEN,

                          access_token_secret=twitter_credentials.ACCESS_TOKEN_SECRET)

# Test authentication
#print(twitter_api.VerifyCredentials())
#creation of test set of 100 tweets with the word cat. we have labelled them already


def build_test_set(search_keyword):
    try:
        tweets_fetched = twitter_api.GetSearch(search_keyword, count=100)
        #print(tweets_fetched)
        print("Fetched " + str(len(tweets_fetched)) + " tweets for the term " +
              search_keyword)
        return[{"text": tweet.text, "label": None} for status in tweets_fetched]
        #get tweets for key word
    except:
        print("unfortunately, something went wrong")
        return None


search_term = input("Enter Search keyword:")
test_data_set = build_test_set(search_term)
training_data_set = []
with open("tweetDataFile.csv", 'rt') as csvfile:
    lineReader = csv.reader(csvfile, delimiter=',', quotechar="\"")
    for row in lineReader:
        training_data_set.append(
            {"tweet_id": row[0], "text": row[1], "label": row[2], "topic": row[3]})


class PreprocessTweets:
    def __init__(self):
        self.stopwords = set(stopwords.words("english") + list(punctuation) +
                             ["AT_USER", "URL"])

    def process_tweets(self, list_of_tweets):
        processed_tweets = []
        for tweet in list_of_tweets:
            if tweet["label"] is not None:
                if tweet["label"] == "positive" or tweet["label"] == "negative":
                    processed_tweets.append(
                        (self._process_tweet(tweet["text"]), tweet["label"]))
            else:
                processed_tweets.append(
                    (self._process_tweet(tweet["text"]), None))
        return processed_tweets


def _process_tweet(self, tweet):
    tweet = tweet.lower()
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)
    tweet = re.sub('@[^\s]+', 'AT_USER', tweet)
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)  # remove the # in #hashtag
    tweet = word_tokenize(tweet)
    words = []
    for word in tweet:
        if word not in self.stopwords:
            words.append(word)
    return words


tweet_processor = PreprocessTweets()
preprocessed_training_set = tweet_processor.process_tweets(training_data_set)
preprocessed_test_set = tweet_processor.process_tweets(test_data_set)


def build_vocabulary(preprocessed_training_data):
    all_words = []
    for (words, sentiment) in preprocessed_training_data:
        all_words.extend(words)
        wordlist = nltk.FreqDist(all_words)
        word_features = wordlist.keys()
    return word_features


training_data_features = build_vocabulary(preprocessed_training_set)


def extract_features(tweet):
    tweet_words = set(tweet)
    features = {}
    for word in training_data_features:
        is_feature_in_words = word in tweet_words
        features[word] = is_feature_in_words
    return features


training_features = nltk.classify.apply_features(extract_features,
                                                 preprocessed_training_set)
NBayesClassifier = nltk.NaiveBayesClassifier.train(training_features)
label = NBayesClassifier.classify(extract_features("I am happy"))
training_features = nltk.classify.apply_features(extract_features,
                                                 preprocessed_training_set)
NBayesClassifier = nltk.NaiveBayesClassifier.train(training_features)
classified_result_labels = []
for tweet in preprocessed_test_set:
    classified_result_labels.append(
        NBayesClassifier.classify(extract_features(tweet[0])))
    if classified_result_labels.count('positive') >= classified_result_labels.count('negative'):
        print("Overall positive sentiment")
        print("Positive Sentiment Percentage = " + str((classified_result_labels.count(
            'positive') / len(classified_result_labels) * 100)) + "%")
    else:
        print("Overall negative sentiment")
        print("Negative Sentiment Percentage = " + str((classified_result_labels.count(
            'negative') / len(classified_result_labels) * 100)) + "%")
