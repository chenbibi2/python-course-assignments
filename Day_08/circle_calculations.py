import math

def choose_radius (radius):
    radius = float(input("Enter the radius of the circle: "))
    
def  calculate_area (radius):
    return math.pi * (radius ** 2)

def calculate_circumference (radius):
    return 2 * math.pi * radius
def Print_results (area,circumference):
    print(f"The area of the circle is: {area:.2f}")
    print(f"The circumference of the circle is: {circumference:.2f}")
