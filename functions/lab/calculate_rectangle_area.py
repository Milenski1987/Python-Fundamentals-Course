def calculate_area(width: int, height: int) -> int:
    return width * height


rectangle_width = int(input())
rectangle_height = int(input())
result = calculate_area(rectangle_width, rectangle_height)

print(result)