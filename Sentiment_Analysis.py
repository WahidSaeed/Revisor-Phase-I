from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
text = input("Enter a text to be analyzed: ")
while text != "quit":
    ss = sid.polarity_scores(text)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
    print()
    text = input("Enter a text to be analyzed: ")
    