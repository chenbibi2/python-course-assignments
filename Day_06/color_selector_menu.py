import sys
filename = sys.argv[1]

with open(filename, 'r') as file:
    colors = [line.strip() for line in file.readlines()]
print("Available colors:")
for color in colors:
    print(f"- {color}")
color_selection = input("Enter a color from the list: ").strip()
if color_selection in colors:
    print(f"You selected {color_selection}.")
else:
    print(f"{color_selection} is not in the list of available colors.")
