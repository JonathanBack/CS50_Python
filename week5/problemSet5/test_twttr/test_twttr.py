from twttr import shorten
def main():
    test_lowercase()
    test_uppercase()
    test_numbers()
    test_empty()

def test_lowercase():
    assert shorten("twitter") == "twttr"

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("TwiTtEr") == "TwTtr"

def test_numbers():
    assert shorten("123!.?") == "123!.?"

def test_empty():
    assert shorten("") == ""

if __name__ == "__main__":
    main()
