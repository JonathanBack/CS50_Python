from bank import value

def test_Hello():
    assert value("hello") == 0

def test_Hs():
    assert value("hi") == 20
    assert value("hey") == 20

def test_others():
    assert value("What's up?") == 100
    assert value("Welcome!") == 100

def test_blankspaces():
    assert value(" Hello ") == 0
    assert value("  Welcome") == 100

def test_upper_lower_case():
    assert value("HeLlo") == 0
    assert value("hEy") == 20
    assert value("WeLcoME") == 100
