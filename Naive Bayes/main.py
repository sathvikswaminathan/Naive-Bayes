# Sentiment Analysis using The Naive Bayes Classifier
import get_reviews 
import NB
from collections import Counter
import math

reviews_dict = get_reviews.extract_reviews() 

class Reviews:
	
	total_reviews_count = len(reviews_dict)

	def __init__(self):
		self.reviews = list()
		self.log_prob = dict() # To prevent underflow

	def instantiate_reviews(self, sentiment): # sentiment = 1-> positive, 0-> negative
		for key, value in reviews_dict.items():
			if sentiment:
				if value > 2:  # sentiment > 2 -> Positive Review 
					self.reviews.append(key)
			else:
				if value <= 2: # sentiment <= 2 -> Negative Review
					self.reviews.append(key)

	def set_probability(self):
		self.prob = self.count/Reviews.total_reviews_count
		self.score = math.log(self.prob)

	def set_tokens(self):
		self.tokens = NB.process_reviews(self.reviews)
		self.count = len(self.tokens)
		self.tokens = dict(Counter(self.tokens))

	def set_log_prob(self):
		for key, value in self.tokens.items():
			self.log_prob[key] = math.log(value/self.count)



positve = Reviews()
negative = Reviews()

positve.instantiate_reviews(1)
negative.instantiate_reviews(0)

positve.set_tokens()
negative.set_tokens()

positve.set_probability()
negative.set_probability()

positve.set_log_prob()
negative.set_log_prob()

sample_review = ["The movie was bad"]

def main():
	
	sentiment = NB.predict_sentiment(sample_review, positve, negative)

	if sentiment:
		print("Positive review")
	else:
		print("Negative review")

if __name__ == '__main__':
	main()
