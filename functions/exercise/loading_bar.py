def loading_bar(percent):
    if percent == 100:
        print(f"100% Complete!\n[%%%%%%%%%%]")
    elif percent == 0:
        print(f"0% [..........]\nStill loading...")
    else:
        percent_count = percent // 10
        print(f"{percent}% [{percent_count * '%'}{(10 - percent_count) * '.'}]\nStill loading...")


loading_bar_percent = int(input())
loading_bar(loading_bar_percent)

