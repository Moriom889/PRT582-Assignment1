
import random
import pytest

# Requirement One

selection_list = ("Scissors","Rock", "Paper", )
def computer_selection(t):

         com_action = random.choice(selection_list)
         print(f"\n computer choses {com_action}.\n")

         return com_action

# Test-cases for function one

def test_case1():
    var = computer_selection("com_action")
    print(f"test_case1 result: {var}")
    assert var in selection_list

def test_case2():
    var = computer_selection("com_action")
    print(f"test_case1 result: {var}")
    assert var in selection_list

def test_case3():
    var = computer_selection("com_action")
    print(f"test_case1 result: {var}")
    assert var in selection_list
