#-------------------- Word Tokenizer --------------------#
# from nltk import word_tokenize

# text = input("Enter a sample text to be tokenized: ")
# tokens = word_tokenize(text)
# print(tokens)


#-------------------- Word Stemming & Lemmatizing --------------------#
# from nltk.stem import PorterStemmer
# from nltk.tokenize import word_tokenize

# ps = PorterStemmer()

# example_words = ["python", "pythoner", "pythoning", "pythoned", "pythonly"]

# for word in example_words:
#     print(ps.stem(word))


#-------------------- POS Tagging --------------------#
# import nltk
# from nltk.corpus import state_union
# from nltk.tokenize import PunktSentenceTokenizer

# train_text = state_union.raw("2005-GWBush.txt")
# sample_text = state_union.raw("2006-GWBush.txt")

# custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

# tokenized = custom_sent_tokenizer.tokenize(sample_text)

# def process_content():
#     try:
#         for i in tokenized:
#             words = nltk.word_tokenize(i)
#             tagged = nltk.pos_tag(words)
#             print(tagged)
#     except Exception as ex:
#         print(ex)

# process_content()

#-------------------- Named Entity Recongnition --------------------#
# import nltk
# from nltk.corpus import state_union
# from nltk.tokenize import PunktSentenceTokenizer

# train_text = state_union.raw("2005-GWBush.txt")
# sample_text = state_union.raw("2006-GWBush.txt")

# custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

# tokenized = custom_sent_tokenizer.tokenize(sample_text)

# def process_content():
#     try:
#         words = nltk.word_tokenize(tokenized[0])
#         tagged = nltk.pos_tag(words)
#         named_entity = nltk.ne_chunk(tagged)
#         named_entity.draw()
#     except Exception as ex:
#         print(ex)

# process_content()

#-------------------- NaiveBayes Classifier --------------------#
# import nltk
# from nltk.corpus import names
# import random

# def gender_feature(input_text):
#     return {'last_letter': input_text[-1]}

# labeled_names = [(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')]
# random.shuffle(labeled_names)

# #featuresets = [(gender_feature(n), gender) for (n, gender) in labeled_names]
# test_set = nltk.classify.apply_features(gender_feature, labeled_names[:500])
# train_set = nltk.classify.apply_features(gender_feature, labeled_names[500:])
# classifier = nltk.NaiveBayesClassifier.train(train_set)
# print('Modal Accuracy: ' + str(nltk.classify.accuracy(classifier, test_set)))

# input_text = ''
# while input_text != 'Quit':
#     input_text = input('Enter a name to be classified: ')
#     print('Gender: ' + classifier.classify(gender_feature(input_text)))

#-------------------- NaiveBayes Classifier (with more than one feature) --------------------#

# import nltk
# import random
# from nltk.corpus import names

# def gender_feature(input_text):
#     return {
#         "Suffix1" : input_text[-1:],
#         "Suffix2" : input_text[-2:],
#     }

# labeled_names = [(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')]
# random.shuffle(labeled_names)
# featuresets = nltk.classify.apply_features(gender_feature, labeled_names)
# train_set, test_set = featuresets[500:], featuresets[:500]
# classifier = nltk.NaiveBayesClassifier.train(train_set)

# print(nltk.classify.accuracy(classifier, test_set))

#-------------------- Document Classification --------------------#

# from nltk.corpus import movie_reviews
# import random
# from nltk import FreqDist

# documents = [(list(movie_reviews.words(fileid)), category)
#                 for category in movie_reviews.categories() 
#                     for fileid in movie_reviews.fileids(category)]

# random.shuffle(documents)
# all_words = FreqDist([word.lower() for word in movie_reviews.words()])
# print(all_words)

from nltk.classify.scikitlearn import  SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB