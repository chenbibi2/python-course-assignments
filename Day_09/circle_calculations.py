import math
    
def  calculate_area (radius):
    """
    This function calculate the area of a circle
    >>> calculate_area (1)
    3.141592654
    >>> calculate_area(2)
    12.56637061
    """
    return math.pi * (radius ** 2)

def calculate_circumference (radius):
    """
    This function calculate the circumference of a circle
    >>> calculate_circumference(1)
    6.283185307
    >>> calculate_circumference(2)
    12.56637061
    """
    return 2 * math.pi * radius
