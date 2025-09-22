import pytest
from tasks._01_basics import add, is_even, factorial, fizzbuzz


def test_add():
    assert add(2, 3) == 5
    assert add(-1.5, 1.5) == 0
    assert add(0, 0) == 0


def test_is_even():
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(0) is True
    assert is_even(-4) is True
    assert is_even(-7) is False


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError):
        factorial(-1)


def test_fizzbuzz():
    assert fizzbuzz(1) == ["1"]
    assert fizzbuzz(3) == ["1", "2", "Fizz"]
    assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert fizzbuzz(15)[-1] == "FizzBuzz"
    # проверка нескольких значений
    out = fizzbuzz(20)
    assert out[2] == "Fizz"      # 3
    assert out[4] == "Buzz"      # 5
    assert out[14] == "FizzBuzz" # 15
    assert out[19] == "Buzz"     # 20
