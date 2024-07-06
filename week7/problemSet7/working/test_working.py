from working import convert
import pytest

def test_no_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"


def test_with_minutes():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_incorrect():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

def test_no_to():
    with pytest.raises(ValueError):
        convert('9 AM - 5 PM')

def test_wrong_hour():
    with pytest.raises(ValueError):
        convert("13 PM to 17 PM")

