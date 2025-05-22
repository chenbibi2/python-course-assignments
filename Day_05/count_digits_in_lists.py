import sys
numbers = [1203, 1256, 312456, 98]
from collections import Counter
digit = ''.join(str(num) for num in numbers)
digit_counts = Counter(digit)
for digit, count in sorted(digit_counts.items()):
            print(f"{digit}: {count}")
print(digit_counts)
