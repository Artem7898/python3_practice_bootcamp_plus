from bot import handle

def test_help():
    assert "Commands" in handle("/help")

def test_echo():
    assert handle("/echo hello world") == "hello world"

def test_sum():
    assert handle("/sum 2 3") == "5.0"
    assert "Numbers only" in handle("/sum a b")
