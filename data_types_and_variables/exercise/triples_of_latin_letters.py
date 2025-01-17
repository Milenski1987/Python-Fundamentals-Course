number_of_symbols = int(input())

for i in range(97, 97 + number_of_symbols):
    for j in range(97, 97 + number_of_symbols):
        for k in range(97, 97 + number_of_symbols):
            print(chr(i) + chr(j) + chr(k))