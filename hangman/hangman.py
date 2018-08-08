import random

def get_secret_word():
    wordfile = "/usr/share/dict/words"
    min_length = 6
    
    good_words = []
    f = open(wordfile)
    for i in f:
        word = i.strip()
        if word.isalpha() and len(word) >= min_length:
            good_words.append(word)
    f.close()

    return random.choice(good_words).lower()

def mask(word, guesses):
    masked_word = []
    for i in word:
        if i in guesses:
            masked_word.append(i)
        else:
            masked_word.append("-")
    return "".join(masked_word)
