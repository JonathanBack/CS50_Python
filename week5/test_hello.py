from hello import hello


#the old hello() does not return any value, only prints it. but the new hello() returns a value, so its TESTABLE

def test_default():

    assert hello() == "hello, world"

def test_argument():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"

