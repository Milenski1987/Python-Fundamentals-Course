def grade_in_words(grade):
    if 2.00 <= grade < 3.00:
        return "Fail"
    elif grade < 3.50:
        return "Poor"
    elif grade < 4.50:
        return "Good"
    elif grade < 5.50:
        return "Very Good"
    elif grade <= 6.00:
        return "Excellent"


grade_in_number = float(input())
result = grade_in_words(grade_in_number)
print(result)