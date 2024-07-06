from um import count

def test_correct():
    assert count("um,") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks for the um...") == 2

def test_words():
    assert count("yummy") == 0
    assert count("corynebacterium") == 0
    assert count("radiothorium") == 0
    assert count("umbilical") == 0
