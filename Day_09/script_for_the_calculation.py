import sys

from circle_calculations import calculate_area, calculate_circumference

def main():
    try: 
    radius = float(input("Enter the radius of the circle: "))
    except (IndexError, ValueError):
       print("Usage: python script_for_the_calculation.py <radius>")  
       return
    area = calculate_area(radius)
    circumference = calculate_circumference(radius)

    print(f"The area of the circle is: {area:.2f}")
    print(f"The circumference of the circle is: {circumference:.2f}")

if __name__ == "__main__":
    main()
