from class1 import main

def test_fun1():
    r : str = main.name
    assert r == "abdul"
    
def test_fun2():
    r : str = main.name
    assert r != "abdul121"