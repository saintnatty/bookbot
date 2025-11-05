def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_amounts(text):
    characters = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0, '.': 0, ' ': 0}
    all_lower = text.lower()
    for character in all_lower:
        if character in characters:
            characters[character] += 1
        if character not in characters:
            characters[character] = character
            characters[character] = 1
    return(characters)


def grab_num_test(to_be_sorted):
    for num in to_be_sorted["num"]:
        return num


def sort_on(characters_dictionary):
    to_be_sorted = []
    for ch, count in characters_dictionary.items():
        to_be_sorted.append({"char": ch, "num": count})
    def grab_num_test(item):
            return item["num"]
    to_be_sorted.sort(reverse=True, key=grab_num_test)
    return(to_be_sorted)




#        print(f"Key: {key}, Value: {characters_dictionary[key]}")
