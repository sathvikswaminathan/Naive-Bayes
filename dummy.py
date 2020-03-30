# Sentiment Analysis using The Naive Bayes Classifier
import re
import math
import pandas as pd
from collections import Counter
from stop_words import get_stop_words

pos_prob = 0.5
neg_prob = 0.5

positive_reviews = list()
negative_reviews = list()
positive_log_prob = dict()
negative_log_prob = dict()
positive_reviews = ["The movie was really good. Could not have got better.", "The movie was amazing"]
negative_reviews = ["The movie was really bad bad bad bad ."]
# instantiate positive_reviews and negative_reviews

stop_words = get_stop_words('english')

# cleaning and processing the reviews 
def process_reviews(reviews):
	tokens = list()
	words = list()
	# tokenization
	for review in reviews:
		tokens += re.findall(r"[\w']+|[.,!?;]", review)
	tokens = [token.lower() for token in tokens]
	# removing non-alphabet expressions (punctuations, html tags, etc) and stop words
	for token in tokens:
		if token.isalpha() and (token not in stop_words or token == "not"):
			words.append(token)
	return words

positive_tokens = process_reviews(positive_reviews)
negative_tokens = process_reviews(negative_reviews)

positive_count = len(positive_tokens)
negative_count = len(negative_tokens)

positive_tokens = dict(Counter(positive_tokens))
negative_tokens = dict(Counter(negative_tokens))

for key, value in positive_tokens.items():
	positive_log_prob[key] = math.log(value/positive_count)
for key, value in negative_tokens.items():
	negative_log_prob[key] = math.log(value/negative_count)

# 1-> positive, 0-> negative
def predict_sentiment(reviews):
	pos_score = math.log(pos_prob)
	neg_score = math.log(neg_prob)
	tokens = process_reviews(reviews)

	for token in tokens:
		if token in positive_log_prob:
			pos_score +=  positive_log_prob[token]
		if token in negative_log_prob:
			neg_score += negative_log_prob[token]

	pos_score = -pos_score
	neg_score = -neg_score

	print(f"Positive Score: {pos_score}")
	print(f"Negative Score: {neg_score}")

	if(pos_score > neg_score):
		return 1
	return 0

sample_text = ["The movie sucked."]

if(predict_sentiment(sample_text)):
	print("Positive review")
else:
	print("Negative review")