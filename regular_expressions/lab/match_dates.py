import re

initial_dates = input()
date_pattern = r"([0-9]{2})([\.\-\/]{1})([A-Z]{1}[a-z]{2})\2([0-9]{4})"

results = re.findall(date_pattern, initial_dates)

for result in results:
    day = result[0]
    month = result[2]
    year = result[3]

    print(f"Day: {day}, Month: {month}, Year: {year}")