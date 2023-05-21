import sys
import os
sys.path.insert(0, os.getcwd())
from multiplication import multiply

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 4) == 0
    assert multiply(-2, 5) == -10
    assert multiply(2.5, 4) == 10.0
    assert multiply(2, -3.5) == -7.0

test_multiply()
