from circle_calculations import calculate_area, calculate_circumference
def main():
    radius = float(input("Enter the radius of the circle: "))
    area = calculate_area(radius)
    circumference = calculate_circumference(radius)
    print(f"The area of the circle is: {area:.2f}")
    print(f"The circumference of the circle is: {circumference:.2f}")
if __name__ == "__main__":
    main()
