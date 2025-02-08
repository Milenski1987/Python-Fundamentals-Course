import re


link_pattern = r"(www\.[A-Za-z0-9\-]+(\.{1}[a-z]+)+)"
links = []

sentence = input()
while sentence:
    results = re.findall(link_pattern, sentence)

    for result in results:
        if result:
            links.append(result[0])
    sentence = input()

for link in links:
    print(link)