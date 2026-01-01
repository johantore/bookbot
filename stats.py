def number_of_words(text):
    words = text.split()
    return len(words)

def char_count(text):
    char = {}
    lowercase = text.lower()
    for character in lowercase:
        if character in char:
            char[character] += 1
        else:
            char[character] = 1
    return char
