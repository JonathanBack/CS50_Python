from fuel import convert
from fuel import gauge
import pytest

def test_convert():
    assert convert("3/4") == 75
    assert convert("1/2") == 50

def test_exceptions():
    with pytest.raises(ValueError):
        convert("2/1")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0.5) == "E"
    assert gauge(99) == "F"
    assert gauge(99.5) == "F"
    assert gauge(50) == "50%"
    assert gauge(37.5) == "37.5%"
