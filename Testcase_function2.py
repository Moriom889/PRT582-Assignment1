import pytest
from function2 import player_selection
import mock
import builtins

# Test-cases

def test_case4():
    with mock.patch.object(builtins, 'input', lambda _: 'Scissors'):
        assert player_selection() == 'Scissors'


def test_case5():
    with mock.patch.object(builtins, 'input', lambda _: 'Paper'):
        assert player_selection() == 'Paper'


def test_case6():
    with mock.patch.object(builtins, 'input', lambda _: 'Rock'):
        assert player_selection() == 'Rock'