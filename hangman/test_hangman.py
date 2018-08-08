import hangman

def test_select_secret_word():
    word = hangman.get_secret_word()
    assert len(word) >= 6
    assert word.islower()
    assert word.isalpha()
    
