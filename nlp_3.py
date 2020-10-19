import nltk
from nltk.corpus import stopwords
from textblob import TextBlob
from pathlib import Path
import pandas as pd

nltk.download("stopwords")
stops = stopwords.words("english")


blob = TextBlob(Path("RomeoAndJuliet.txt").read_text())

"""

print(stops)

new_blob = [word for word in blob.words if word not in stops]

print(new_blob)

"""

items = blob.word_counts.items()
print(items)
print("\n\n")

new_items = [i for i in items if i[0] not in stops]
print(new_items)

from operator import itemgetter

sorted_items = sorted(items, key = itemgetter(1), reverse = True)

top20 = sorted_items[:20]

df = pd.DataFrame(top20, columns = ["word", "count"])
print(df)




plt.gcf().tight_layout
plt.show()
