import sys
import os
sys.path.insert(0, os.getcwd())
from addition import add, subtract

def test_math_functions():
    assert add(2, 3) == 5
    assert add(-2, 3) == 1
    assert add(0, 0) == 0
    assert subtract(5, 2) == 3
    assert subtract(-5, -2) == -3
    assert subtract(0, 0) == 0

test_math_functions()
