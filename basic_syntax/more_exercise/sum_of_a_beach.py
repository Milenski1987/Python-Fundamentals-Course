string = input()

string = string.lower()
sand = string.count("sand")
water = string.count("water")
fish = string.count("fish")
sun = string.count("sun")
count = sand + water + fish + sun
print(count)