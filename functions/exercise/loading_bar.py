def loading_bar(percent: int) -> str:
    if percent == 100:
        return f"100% Complete!\n[%%%%%%%%%%]"
    percents_count = percent // 10
    dots_count = 10 - percents_count
    return f"{percent}% [{percents_count * '%'}{dots_count * '.'}]\nStill loading..."


loading_bar_percent = int(input())
result = loading_bar(loading_bar_percent)

print(result)