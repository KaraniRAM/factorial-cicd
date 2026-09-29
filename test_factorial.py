import pytest
from factorial import  factorial 
def test_0():
    assert factorial(0)==1
def test_5():
    assert factorial(5)==120
def test_8():
    assert factorial(8)==40320
def test_10():
    assert factorial(10)==3628800
def test_12():
    assert factorial(12)==479001600
def test_negative():
    with pytest.raises(ValueError):
        factorial(-34)