from bank import pay

def test_bank_Honly():
    assert pay('hey') == 20   
    assert pay ('Hola') == 20

def test_bank_hello():    
    assert pay('hello') == 0
    assert pay ('HELLO') == 0
    
def test_bank_notH():
    assert pay ('abcde') == 100
    assert pay ('01234') == 100