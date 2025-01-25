def palindrome(list_numbers):
    for number in list_numbers:
        if number == number[::-1]:
            print("True")
        else:
            print("False")

list_of_integers = input().split(", ")
palindrome(list_of_integers)