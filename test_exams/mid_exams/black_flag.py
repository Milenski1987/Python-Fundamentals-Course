def get_or_lose_plunder(days: int, daily: int) -> float:
    result = 0
    for day in range(1, days + 1):
        result += daily
        if day % 3 == 0:
            result += daily * 0.50
        if day % 5 == 0:
            result -= result * 0.30
    return result


def check_goals(expected: float, collected: float) -> str:
    if collected >= expected:
        return f"Ahoy! {collected:.2f} plunder gained."
    percent = collected / expected * 100
    return f"Collected only {percent:.2f}% of the plunder."


def main():
    days_of_plunder = int(input())
    daily_plunder = int(input())
    expected_plunder = float(input())

    collected_plunder = get_or_lose_plunder(days_of_plunder, daily_plunder)

    print(check_goals(expected_plunder, collected_plunder))


main()