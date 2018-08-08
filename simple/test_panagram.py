import exercise

def test_panagram_false():
    sentence = "the quick brown fox jumped over the lazy dog" # s is missing
    assert exercise.panagram(sentence) == False

    
    
