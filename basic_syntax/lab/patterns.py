max_stars = int(input())

for i in range(1, max_stars + 1):
    print(i * "*")

for j in range(max_stars - 1, 0, -1):
    print(j * "*")