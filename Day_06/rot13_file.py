import sys 
import codecs
filename = sys.argv[1]
with open(filename, 'r') as file:
  content = file.read()
apply_ROT13 = codecs.encode(content, 'rot_13')
with open(filename, 'w') as file:
  file.write(apply_ROT13)
