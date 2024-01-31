import pytest
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