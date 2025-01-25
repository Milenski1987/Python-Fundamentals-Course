def grade_in_words(grade):
    result= ""
    if 2.00 <= grade < 3.00:
        result = "Fail"
    elif grade < 3.50:
        result = "Poor"
    elif grade < 4.50:
        result = "Good"
    elif grade < 5.50:
        result = "Very Good"
    elif grade <= 6.00:
        result = "Excellent"

    return result

grade_in_number = float(input())
print(grade_in_words(grade_in_number))