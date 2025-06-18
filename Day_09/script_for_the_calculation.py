from circle_calculations import choose_radius, calculate_area, calculate_circumference, print_results

def main():
    radius = choose_radius()
    area = calculate_area(radius)
    circumference = calculate_circumference(radius)
    print_results(area, circumference)

if __name__ == "__main__":
    main()
