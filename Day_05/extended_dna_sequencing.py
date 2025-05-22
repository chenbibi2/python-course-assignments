import sys
import re
sequence = input ("Please type in a sequence:")
segments = re.split(r'[^ACTG]', sequence)
segments = [seg for seg in segments if seg]
sorted_seq = sorted(segments, key=len, reverse=True)
print (sorted_seq)
