import argparse
import sys

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="cli_calc", description="Простой CLI‑калькулятор")
    sub = parser.add_subparsers(dest="cmd", required=True)
    for name in ("add", "sub", "mul", "div"):
        p = sub.add_parser(name, help=f"{name} two integers")
        p.add_argument("a", type=float)
        p.add_argument("b", type=float)
    return parser

def main(argv=None) -> int:
    argv = argv or sys.argv[1:]
    parser = build_parser()
    ns = parser.parse_args(argv)
    a, b = ns.a, ns.b
    match ns.cmd:
        case "add": print(a + b)
        case "sub": print(a - b)
        case "mul": print(a * b)
        case "div":
            if b == 0:
                print("Error: division by zero", file=sys.stderr)
                return 2
            print(a / b)
        case _:
            parser.print_help()
            return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
