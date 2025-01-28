money_for_beggars = [int(number) for number in input().split(", ")]
number_of_beggars = int(input())
beggars_earnings = []


for beggar in range(number_of_beggars):
    beggar_money = 0
    for money_index in range(beggar, len(money_for_beggars), number_of_beggars):
        beggar_money += money_for_beggars[money_index]

    beggars_earnings.append(beggar_money)

print(beggars_earnings)
