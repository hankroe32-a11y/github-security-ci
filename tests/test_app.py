from src.app import add, multiply

def test_add():
    assert add(2, 3) == 5

def test_mutliply():
    assert multiply(4, 5) == 20
