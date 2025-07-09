import pytest
from calc import add
from calc import subtract
from calc import multiply
from calc import divide

@pytest.mark.parametrize("a,b,expected", [
    (10, 2, 12),
    (7, 3, 10),
    (0, 5, 5),
])

def test_add(a, b, expected):
    result = add(a, b)
    assert result == expected, f"결과가 예상과 다릅니다. 결과 : {result}"

@pytest.mark.parametrize("a,b,expected", [
    (10, 2, 8),
    (7, 3, 4),
    (0, 5, -5),
])

def test_subtract(a, b, expected):
    result = subtract(a, b)
    assert result == expected, f"결과가 예상과 다릅니다. 결과 : {result}"

@pytest.mark.parametrize("a,b,expected", [
    (10, 2, 20),
    (7, 3, 21),
    (0, 5, 0),
])

def test_multiply(a, b, expected):
    result = multiply(a,b)
    assert result == expected, f"결과가 예상과 다릅니다. 결과 : {result}"

@pytest.mark.parametrize("a,b,expected", [
    (10, 2, 5),
    (7, 3, 7/3),
    (0, 5, "Error : Cannot divide by zero"),
])

def test_divide(a, b, expected):
    result = divide(a, b)
    assert result == expected, f"결과가 예상과 다릅니다. 결과 : {result}"