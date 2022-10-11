import pytest
from function4 import is_get_enough_point

# testcase
def test_case13():
    var = is_get_enough_point(5, 5)
    print(f"test_case13 result: {var}")
    assert var == True

def test_case14():
    var = is_get_enough_point(4, 5)
    print(f"test_case14 result: {var}")
    assert var == False

def test_case15():
    var = is_get_enough_point(5, 5)
    print(f"test_case15 result: {var}")
    assert var == True


def test_case16():
    var = is_get_enough_point(3, 5)
    print(f"test_case16 result: {var}")
    assert var == False
