def calculate_area(length, width):
    area = length * width
    return area


def calculate_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter

def calculate_area_perimeter(length, width):
    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)
    return area, perimeter