from math import sqrt, floor


def distance(x, y):
    length = sqrt(((x - 0) ** 2) + ((y - 0) ** 2))
    return length


def compare(p1x, p1y, p2x, p2y):
    distance_p1 = distance(p1x, p1y)
    distance_p2 = distance(p2x, p2y)

    if distance_p1 <= distance_p2:
        return f"({p1x}, {p1y})"
    else:
        return f"({p2x}, {p2y})"


x1 = floor(float(input()))
y1 = floor(float(input()))
x2 = floor(float(input()))
y2 = floor(float(input()))

print(compare(x1, y1, x2, y2))

