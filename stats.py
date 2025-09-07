def get_num_words(text_to_split):
    
    list_of_words = text_to_split.split()
    return len(list_of_words)


def get_num_of_characters(text_file):
    chars = {}
    for c in text_file:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(items):
    return items["num"]

def sort_characters(char_dict):
    
    sorted_List = []
    for ch in char_dict:
        sorted_List.append({"char": ch, "num": char_dict[ch]})
    sorted_List.sort(reverse=True, key=sort_on)
    return sorted_List