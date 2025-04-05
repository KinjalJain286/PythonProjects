def reverse_character_order(text):
    return text[::-1]

def reverse_word_order(text):
    words = text.split()
    return ' '.join(reversed(words))