from pathlib import Path
from textblob import TextBlob as tb

blob = tb(Path("RomeoAndJuliet.txt").read_text())

print(blob.words.count("joy"))
print("\n\n")

print(blob.noun_phrases.count("lady capulet"))
print("\n\n")

from textblob import Word

happy = Word("happy")

# Princeton database dictionary
print(happy.definitions)
print("\n\n")

# Synonyms
print(happy.synsets)
print("\n\n")
