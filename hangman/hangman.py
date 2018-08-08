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


def process(state, guess):
    word = state['word']
    guesses = state['guesses'][:]
    if guess in word:
        tries_left = state['tries_left']
    else:
        tries_left = state['tries_left'] - 1

    if guess not in guesses:
        guesses.append(guess)
    
    state = dict(tries_left = tries_left,
                 guesses = guesses,
                 word = word)
    return  state

def status_message(state):
    guesses = ", ".join(state['guesses'])
    status_message = """Word: {}
Guesses: {}
Tries left: {}
""".format(mask(state['word'], state['guesses']),
           guesses,
           state['tries_left'])
    return status_message
                
   
    
    
