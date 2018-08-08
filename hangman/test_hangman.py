import hangman

def test_select_secret_word():
    word = hangman.get_secret_word()
    assert len(word) >= 6 , "{} is less than 6 letters long".format(word)
    assert word.islower(), "{} is not all lower".format(word)
    assert word.isalpha(), "{} is not all alphabetical".format(word)

def test_select_multiple_secret_words():
    words = set()
    for i in range(10):
        words.add(hangman.get_secret_word())
    assert len(words) == 10

def test_mask_word():
    assert hangman.mask("elephant", []) == "--------"
    assert hangman.mask("elephant", ['x', 'q']) == "--------"
    assert hangman.mask("elephant", ['t', 'q']) == "-------t"
    assert hangman.mask("elephant", ['t', 'e']) == "e-e----t"


def test_guesses_bad_guess():
    state = dict(tries_left = 10,
                 guesses = [],
                 word = "elephant")
    new_state = hangman.process(state, 'q')
    assert new_state['tries_left'] == 9
    assert new_state['guesses'] == ['q']

def test_guesses_good_guess():
    state = dict(tries_left = 10,
                 guesses = [],
                 word = "elephant")
    new_state = hangman.process(state, 't')
    assert new_state['tries_left'] == 10
    assert new_state['guesses'] == ['t']

def test_status_message():
    state = dict(tries_left = 7,
                 guesses = ['p', 'e', 'q'],
                 word = "elephant")
    status = hangman.status_message(state)

    expected = """Word: e-ep----
Guesses: p, e, q
Tries left: 7
"""
    assert status == expected





