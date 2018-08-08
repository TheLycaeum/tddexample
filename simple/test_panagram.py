import exercise

def test_panagram_false():
    sentence = "the quick brown fox jumped over the lazy dog" # s is missing
    assert exercise.panagram(sentence) == False

def test_panagram_true():
    sentence = "the quick brown fox jumps over the lazy dog" 
    assert exercise.panagram(sentence) == True
    
def test_panagram_false_mixed_case():
    sentence = "The quick brown fox jumped over the lazy dog" # s is missing
    assert exercise.panagram(sentence) == False

def test_panagram_true_mixed_case():
    sentence = "The quick brown fox jumps over the lazy dog" 
    assert exercise.panagram(sentence) == True

def test_panagram_false_with_punctuation():
    sentence = "The quick brown fox jumped over the lazy dog." # s is missing
    assert exercise.panagram(sentence) == False

def test_panagram_true_with_punctuation():
    sentence = "The quick brown fox jumps over the lazy dog."
    assert exercise.panagram(sentence) == True
