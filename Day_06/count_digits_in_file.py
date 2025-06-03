import sys
from collections import Counter
filename = sys.argv[1]
output_filename = "report.txt" 
with open(filename, 'r') as file:
    content = file.read()
digit = ''.join(filter(str.isdigit, content))
digit_counts = Counter(digit)
for digit, count in sorted(digit_counts.items()):
            print(f"{digit}: {count}")
print(digit_counts)

with open(output_filename, 'w') as output_file:
    for digit, count in sorted(digit_counts.items()):
        output_file.write(f"{digit}: {count}\n")
