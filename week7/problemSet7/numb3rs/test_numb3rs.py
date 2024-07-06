import pytest
from numb3rs import validate

def test_correct():
    assert validate("255.255.255.255") == True
    assert validate("127.0.0.1") == True

def test_incorrect():
     assert validate("512.512.512.512") == False
     assert validate("1.2.3.1000") == False
     assert validate("10.10.10.10.10.10.10") == False
     assert validate("1.1.1") == False
     assert validate("127.1.3.512") == False
def test_str():
      assert validate("cat") == False
