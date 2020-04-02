# Sentiment Analysis using the Naive Bayes Classifier

The data to train this classifier comes from the Kaggle Challenge - [Sentiment Analysis on Movie Reviews](https://www.kaggle.com/c/sentiment-analysis-on-movie-reviews/data)

## This classifier exploits the Bayes theorem which allows us to calculate Conditional Probability.

## There are three classifications of the Naive Bayes Classifier:
* Gaussian Naive Bayes Classifier:
It is used when the feautures are continous. The feautures are assumed to have a normal distribution allowing us to calculate the probability for values we haven't seen in our data set before.

* Bernoulli Naive Bayes Classifier:
It is used when the features are binary ( 0 or 1, absent or present, good or bad, etc.)

* Multinomial Naive Bayes Classifier:
It is used when the features are nothing but discrete counts. For example, in this repository, a Multinomial NB has been implemented as the count of words in the Movie reviews are discrete which act as the feautures for our model. 

The Naive Bayes Classifier has two terms to it:
* Bayes: The probability of an entity belonging to a particular class is computed using the *Bayes* theorem

* Naive: All the features are assumed to be independent of each other because it simplifies the mathematics of computing the probability  but it is a *Naive* assumption because this is not at all the case. Example: If the algorithm is trying to determine if a person is a boy or a girl given certain features like Height, weight, size of foot, etc. We know that these features are dependent of each other and our assumption does not hold true. But this works well in practise and it reduces the complexity of our computation.

![Result](https://github.com/sathvikswaminathan/Sentiment-Analysis/raw/master/Naive%20Bayes/result.png)

