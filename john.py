import nltk
from nltk.corpus import stopwords
from textblob import TextBlob
from pathlib import Path
from wordcloud import WordCloud
import imageio

nltk.download("stopwords")
stops = stopwords.words("english")

old_john = TextBlob(Path("book of John text.txt").read_text())
john = old_john.split()

# Creates new list of words containing no machine code
new_john = [jan for jan in john if jan not in stops]

# This block converts the book of John into string tokens.
# If any of these tokenized words match qualifies as "noun" part of speech
# the noun will be sent the list, "noun_john" - a frequency distribution is constructed from the list of nouns
# .most_common(x) can be used to return a tuple of "x" most common words and a counter
is_noun = lambda pos: pos[:2] == 'NN'
tokenized_john = nltk.word_tokenize(str(old_john))
noun_john = [word for (word, pos) in nltk.pos_tag(tokenized_john) if is_noun(pos)] 
stopwords = nltk.corpus.stopwords.words('english')
john_frequency = nltk.FreqDist(w.lower() for w in noun_john if w not in stopwords)
top15_johns = john_frequency.most_common(15)
john_wc = " ".join([str(jee) for jee in top15_johns])

print("\n", top15_johns, "\n")

john_cloud = WordCloud(colormap = "Pastel2", background_color = "gray", max_words = 15).generate(john_wc)
john_cloud = john_cloud.to_file("john.png")
