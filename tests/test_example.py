import pytest

from example_project import multiply


@pytest.mark.parametrize("x,y,res", [
    (1, 1000, 1000),
    (2, 0.5, 1),
    (5, 5, 25),
])
def test_multiply(x, y, res):
    assert multiply(x, y) == res
