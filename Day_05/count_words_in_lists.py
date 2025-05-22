from collections import Counter
celestial_objects = ['Moon', 'Gas', 'Asteroid', 'Dwarf', 'Asteroid', 'Moon', 'Asteroid']
words = ' '.join(celestial_objects).split()
word_counts = Counter(words)
for word, count in sorted(word_counts.items()):
    print(f"{word}: {count}")
