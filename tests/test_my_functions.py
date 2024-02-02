import pytest
import time
import source.my_functions as my_functions

def test_add():
    result = my_functions.add(1,4)
    assert result == 5

def test_add_string():
    result = my_functions.add('asd','zxc')
    assert result == 'asdzxc'

def test_devide():
    result = my_functions.divide(4,2)
    assert result == 2

def test_devide_by_zero():
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(10,0)

@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_functions.divide(4, 2)
    assert result == 2

@pytest.mark.skip(reason="This is broken")
def test_add():
    assert my_functions.add(1,2) == 3

@pytest.mark.xfail(reason='We know that we cannot divide by zero')
def test_divide_by_zero_broken():
    my_functions.divide(4,0)