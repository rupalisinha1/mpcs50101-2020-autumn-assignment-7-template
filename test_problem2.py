import pytest
from fraction import Fraction

    
def test_initialization():
    """Test fraction creation"""
    f1 = 0.625
    f = Fraction(5,8) 
    assert f.__str__() == "5/8"
    assert f.as_decimal == 0.625
    # Add a test to not allow a denominator is 0

def test_add():
    """Test the addition function"""
    f1 = Fraction(5,8) 
    f2 = Fraction(5,8) 

    add_them_up = f1 + f2
    assert add_them_up.__str__() != "10/8" 
    assert add_them_up.__str__() != "5/4" 
    assert add_them_up.__str__() == "1-1/4" 
    assert add_them_up.as_decimal == 1.25
  
def test_subtract():
    """Test the addition function"""
    f1 = Fraction(1,2) 
    f2 = Fraction(2,1) 

    total = f1 / f2
    assert total.__str__() == "1/4" 
    assert total.as_decimal == 0.25


def test_multiply():
    """ """
    f1 = Fraction(5,8) 
    f2 = Fraction(2/1)
    f3 = f1 * f2
    assert f3.__str__() != "10/8"
    assert f3.as_decimal == 1.25

def test_divide():
    """ """
    f1 = Fraction(5,8) 
    f2 = Fraction(1,1)
    f3 = f1 / f2
    assert f3.__str__() != "5/8"
    assert f3.as_decimal == 0.625
