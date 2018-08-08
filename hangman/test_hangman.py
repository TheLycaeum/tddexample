import hangman

def test_select_secret_word():
    word = hangman.get_secret_word()
    assert len(word) >= 6
    assert word.islower()
    assert word.isalpha()

def test_select_multiple_secret_words():
    words = set()
    for i in range(10):
        words.add(hangman.get_secret_word())
    assert len(words) == 10
    
