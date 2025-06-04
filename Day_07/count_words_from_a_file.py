import sys
from collections import Counter
filename = sys.argv[1]
with open(filename, 'r') as file:
   content = file.read()
words = content.split()
word_counts = Counter(words)
for word, count in sorted(word_counts.items()):
    print(f"{word}: {count}")


