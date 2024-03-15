from lab2 import multiply
import pytest
def test_multiply():
    assert multiply(5, 8) == 40
    assert multiply(0, 0) == 0
    assert multiply(3, -2) == -6