from twttr import shorten

def test_shorten():
    assert shorten("AEIOUaeiou.,/xyz") == ".,/xyz"
