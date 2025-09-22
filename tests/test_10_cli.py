import pytest
pytestmark = pytest.mark.skip(reason="Разблокируйте, когда будете готовы.")

from tasks._10_cli import build_parser


def run_cli(argv):
    parser = build_parser()
    ns = parser.parse_args(argv)
    return ns, parser


def test_greet(capsys):
    ns, parser = run_cli(["greet", "--name", "Artem"])
    # тест не требует печати, но проверьте, что аргументы распознаны
    assert ns.command == "greet"
    assert ns.name == "Artem"


def test_add():
    ns, _ = run_cli(["add", "2", "40"])
    assert ns.command == "add"
    assert ns.a == 2 and ns.b == 40
