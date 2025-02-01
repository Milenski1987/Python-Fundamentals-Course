def create_dictionary(synonyms_dictionary: dict, words_count: int) -> dict:
    for _ in range(words_count):
        word = input()
        synonym = input()

        if word not in synonyms_dictionary:
            synonyms_dictionary[word] = []
        synonyms_dictionary[word].append(synonym)
    return synonyms_dictionary

def main():
    number_of_words = int(input())
    synonyms = {}

    synonyms = create_dictionary(synonyms, number_of_words)

    for word, synonym in synonyms.items():
        print(f"{word} - {', '.join(synonym)}")


main()