words_list = input().split()
palindrome = input()

result = [word for word in words_list if word[::-1] == word]
print(result)
palindromes_in_result = result.count(palindrome)
print(f"Found palindrome {palindromes_in_result} times")