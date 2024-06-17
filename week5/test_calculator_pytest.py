############################################################################################################################
#
#
#                                               TESTING WITH PYTEST
# instead of writing python file.py on terminal, write pytest file.py on terminal
#
############################################################################################################################
from calculator import square
import pytest
'''
def test_square():
    assert square(2) == 4
    assert square(3) == 9 <- PYTEST WILL RETURN THIS ONE AS A FAILURE AND STOP HERE
    assert square(-2) == 4 <- PYTEST WONT EVEN TEST THIS ONE IF THE ONES ABOVE FAIL
    assert square(-3) == 9
    assert square(0) == 0
'''
#the first assert that fails will be displayed on terminal, but what if there are more tests failling as well?
#In order to catch as many fails as possible you can do multiple separeted tests of different categories

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")
