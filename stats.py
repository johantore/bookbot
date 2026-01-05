def number_of_words(text):
    words = text.split()
    return len(words)

def char_count(text):
    char = {}
    lowercase = text.lower()
    for character in lowercase:
        if character.isalpha() == False:
            continue
        if character in char:
            char[character] += 1
        else:
            char[character] = 1
    return char

def sort_key(text):
    return text["num"]

def char_sort(char_list):
    sorted_list = []
    for char in char_list:
        sorted_list.append({"char": char, "num": char_list[char]})
    sorted_list.sort(reverse=True, key=sort_key)
    return sorted_list
