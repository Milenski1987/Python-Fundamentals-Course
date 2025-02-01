def distribution(people: list, poor_threshold: int) -> list:
    for index in range(len(people)):
        if people[index] < poor_threshold:
            difference = poor_threshold - people[index]
            max_wealth_index = people.index(max(people))
            people[index] += difference
            people[max_wealth_index] -= difference
    return people


def check_social_distribution(people: list, poor_threshold: int):
    for element in people:
        if element < poor_threshold:
            return "No equal distribution possible"
    return people


def main():
    population = [int(number) for number in input().split(", ")]
    minimum_wealth = int(input())

    population = distribution(population, minimum_wealth)
    result = check_social_distribution(population, minimum_wealth)

    print(result)


main()



