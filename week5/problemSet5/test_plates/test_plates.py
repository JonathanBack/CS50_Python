'''
Among the requirements, though, are:

    “All vanity plates must start with at least two letters.”
    “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable vanity
    plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
    “No periods, spaces, or punctuation marks are allowed."
'''

from plates import is_valid

def test_starts_with_2ormore_letters():
    assert is_valid("AA2342") == True
    assert is_valid("BB2342") == True
    assert is_valid("CCC342") == True
    assert is_valid("ZZZ342") == True
    assert is_valid("123456") == False

def test_lenght():
    assert is_valid("AB12345") == False
    assert is_valid("A") == False

def test_text_numbers():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False

def test_first_number():
    assert is_valid("AA0123") == False
    assert is_valid("BB0123") == False

def test_spaces_punct():
    assert is_valid("AA123@") == False
    assert is_valid("AA 23@") == False
    assert is_valid("AA!@#$") == False
    assert is_valid("AA?/23") == False
