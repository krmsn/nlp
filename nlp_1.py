from textblob import TextBlob 

text = "Today is a beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)

print(blob.sentences)
print("\n\n")

print(blob.words)
print("\n\n")

print(blob.tags)
print("\n\n")

print(blob.noun_phrases)
print("\n\n")

print("Polarity Rating:", round(blob.sentiment.polarity, 3))
print("\n\n")

print("Subjectivity Rating:", round(blob.sentiment.subjectivity, 3))
print("\n\n")

sentences = blob.sentences

"""

for sentence in sentences:
    print(sentence)
    print("\n\n")

    print(sentence.sentiment)
    print("\n\n")

    print(round(sentence.sentiment.polarity, 3))
    print("\n\n")

    print(round(sentence.sentiment.subjectivity, 3))
    print("\n\n")

"""

from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer = NaiveBayesAnalyzer())

"""

print(blob.sentiment)
print("\n\n")

sentences = blob.sentences
print(blob.detect_language)
print("\n\n")

spanish = blob.translate(to = "es")
print(spanish)
print("\n\n")

viet = blob.translate(to = "vi")
print(viet)
print("\n\n")

en = viet.translate()
print(en)

"""

from textblob import Word

index = Word("Index")
print(index.pluralize())
print("\n\n")

animals = TextBlob("dog cat fish sheep bird").words
print(animals.pluralize())
print("\n\n")

cacti = Word("cacti")
print(cacti.singularize())
print("\n\n")

word = Word("Theyr")
print(word.spellcheck())
print("\n\n")

word.correct()
print(word)
print("\n\n")

sentence = str("This sentence has a misspelled word in it.")
sentence = sentence.correct()
print(sentence)
print("\n\n")
