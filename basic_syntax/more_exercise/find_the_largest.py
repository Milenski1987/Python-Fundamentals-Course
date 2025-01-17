number = input()
numbers = [int(num) for num in number]
numbers = sorted(numbers, reverse=True)
print(*numbers,sep="")
