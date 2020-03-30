import pandas as pd 

# extracting sentiment and reviews
def extract_reviews():
	reviews_read = pd.read_csv("train.tsv", sep='\t')

	Sentiment_col = reviews_read["Sentiment"]
	Phrase_col = reviews_read["Phrase"]
	Sentiment_col = Sentiment_col.tolist()
	Phrase_col = Phrase_col.tolist()

	reviews_dict = dict(zip(Phrase_col, Sentiment_col))

	return reviews_dict