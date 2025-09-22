from cli_calc import main

def run(argv):
    import io, sys
    out, err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    sys.stdout, sys.stderr = out, err
    try:
        code = main(argv)
    finally:
        sys.stdout, sys.stderr = old_out, old_err
    return code, out.getvalue().strip(), err.getvalue().strip()

def test_add():
    code, out, err = run(["add","2","3"])
    assert code == 0 and out == "5.0"

def test_div_zero():
    code, out, err = run(["div","2","0"])
    assert code == 2 and "division by zero" in err
