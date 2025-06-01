def get_word_count(text):
    count = text.split()
    return len(count)

def get_letter_dict(text):
    letters = {}
    for letter in text:
        lower_case = letter.lower()
        if lower_case in letters:
            letters[lower_case] += 1
        else:
            letters[lower_case] = 1
    return letters

def sort_on(d):
    return d["num"]

def sort_dict_to_list(letter_dict):
    sorted_list = []
    for letter in letter_dict:
        sorted_list.append({"char": letter, "num": letter_dict[letter]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
