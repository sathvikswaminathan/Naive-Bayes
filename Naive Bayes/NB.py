import re
from stop_words import get_stop_words

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

# 1-> positive, 0-> negative
def predict_sentiment(reviews, positive, negative):
	tokens = process_reviews(reviews)
	
	for token in tokens:
		if token in positive.log_prob:
			positive.score +=  positive.log_prob[token]
		if token in negative.log_prob:
			negative.score += negative.log_prob[token]

	# print(f"Positive Score: {positive.score}")
	# print(f"Negative Score: {negative.score}")

	if(positive.score > negative.score):
		return 1
	return 0
