import pytest
pytestmark = pytest.mark.skip(reason="Разблокируйте, когда будете готовы.")

from tasks._04_oop import Stack, Temperature


def test_stack_basic():
    st = Stack()
    assert st.is_empty()
    st.push(1)
    st.push(2)
    assert len(st) == 2
    assert st.peek() == 2
    assert st.pop() == 2
    assert st.pop() == 1
    assert st.is_empty()
    with pytest.raises(IndexError):
        st.pop()


def test_temperature():
    t = Temperature(0.0)
    assert t.celsius == 0.0
    assert round(t.fahrenheit, 2) == 32.0
    t.fahrenheit = 212.0
    assert round(t.celsius, 2) == 100.0
