import pytest
from function3 import winner_each_round

def test_case7():
    var = winner_each_round('scissors', 'Rock')
    assert var == 2
def test_case8():
    var = winner_each_round('Paper', 'Scissors')
    assert var == 2
def test_case9():
    var = winner_each_round('Scissors', 'Paper')
    assert var == 1

def test_case10():
    var = winner_each_round('Rock', 'Paper')
    assert var == 2
def test_case11():
    var = winner_each_round('Paper', 'Rock')
    assert var == 1
def test_case12():
    var = winner_each_round('Rock', 'scissors')
    assert var == 1

