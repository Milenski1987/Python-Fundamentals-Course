population = [int(number) for number in input().split(", ")]
minimum_wealth = int(input())

for index in range(len(population)):
    if population[index] < minimum_wealth:
        difference = minimum_wealth - population[index]
        max_wealth_index = population.index(max(population))
        population[index] += difference
        population[max_wealth_index] -= difference

for element in population:
    if element < minimum_wealth:
        print("No equal distribution possible")
        break
else:
    print(population)