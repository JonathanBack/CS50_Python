from jar import Jar
import pytest

def test_init():

    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar = Jar(-1)
    with pytest.raises(ValueError):
        jar = Jar(1.5)

def test_str():

    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():

    jar = Jar(10)
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(1)
    assert jar.size == 2

    with pytest.raises(ValueError):
        jar.deposit(15)

def test_withdraw():

    jar = Jar(10)
    jar.deposit(10)
    jar.withdraw(5)
    assert jar.size == 5
    jar.withdraw(5)
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar.withdraw(20)
