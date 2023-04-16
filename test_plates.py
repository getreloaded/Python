from plates import is_valid

def test_is_valid():
    assert is_valid("123456") == False          # starts with alpha
    assert is_valid("A12345") == False          # starts with alpha for first two
    assert is_valid("abcd1234") == False        # length is more than 6
    assert is_valid("A") ==  False              # length is less than 2
    assert is_valid("ac.123") ==  False         # no symbols only alpha numeric
    assert is_valid("abcdef") == True           # no numbers
    assert is_valid("ABC023") == False          # no 0 after Alpha
    assert is_valid("AB1234") == True           # Correct num plate
