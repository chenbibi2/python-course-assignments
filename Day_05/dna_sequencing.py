import sys
# here it takes the sequence from the user
sequence = sys.argv[1]
cleaned = [s for s in sequence.split('X') if s.strip()]
print(cleaned) 
# sort by lenght 
cleaned_length = sorted(cleaned, key=len, reverse=True)
print(cleaned_length) 
