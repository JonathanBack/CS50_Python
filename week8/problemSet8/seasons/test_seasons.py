from seasons import get_sentence, get_diff

def test_get_sentence():
    assert get_sentence(571680) == "Five hundred seventy-one thousand, six hundred eighty"
    assert get_sentence(1052640) == "One million, fifty-two thousand, six hundred forty"
    assert get_sentence(483840) == "Four hundred eighty-three thousand, eight hundred forty"

def test_get_diff():
    assert get_diff("2023-05-30") == 571680
    assert get_diff("2022-06-30") == 1052640
    assert get_diff("2023-07-30") == 483840
