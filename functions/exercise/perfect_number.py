def perfect_number(num):
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i

    if divisors_sum == num:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


number = int(input())
perfect_number(number)

