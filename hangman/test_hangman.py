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


