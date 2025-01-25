from math import sqrt, floor


def line_length_and_distance_to_center(x1, y1, x2, y2):
    length = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    return length


def line_compare():
    first_line_length = line_length_and_distance_to_center(l1p1x, l1p1y, l1p2x, l1p2y)
    second_line_length = line_length_and_distance_to_center(l2p1x, l2p1y, l2p2x, l2p2y)

    if first_line_length >= second_line_length:
        first_point_distance = line_length_and_distance_to_center(0, 0, l1p1x, l1p1y)
        second_point_distance = line_length_and_distance_to_center(0, 0, l1p2x, l1p2y)
        if first_point_distance <= second_point_distance:
            return f"({l1p1x}, {l1p1y})({l1p2x}, {l1p2y})"
        elif first_point_distance > second_point_distance:
            return f"({l1p2x}, {l1p2y})({l1p1x}, {l1p1y})"
    else:
        first_point_distance = line_length_and_distance_to_center(0, 0, l2p1x, l2p1y)
        second_point_distance = line_length_and_distance_to_center(0, 0, l2p2x, l2p2y)
        if first_point_distance <= second_point_distance:
            return f"({l2p1x}, {l2p1y})({l2p2x}, {l2p2y})"
        elif first_point_distance > second_point_distance:
            return f"({l2p2x}, {l2p2y})({l2p1x}, {l2p1y})"


l1p1x = floor(float(input()))
l1p1y = floor(float(input()))
l1p2x = floor(float(input()))
l1p2y = floor(float(input()))
l2p1x = floor(float(input()))
l2p1y = floor(float(input()))
l2p2x = floor(float(input()))
l2p2y = floor(float(input()))
print(line_compare())

