import sys

sys.path.append("../../")
from calc_service.modules.simple_calc import SimpleCalculator


def test_without_first_plus():
    x = "+100.1"  # → 100.1
    testfoo = SimpleCalculator()
    result = testfoo.calculation_from_string(x)
    assert result == "100.1"


def test_minus_before_zero():
    x = "-0"  # → 0
    testfoo = SimpleCalculator()
    result = testfoo.calculation_from_string(x)
    assert result == "0"


def test_round_up():
    x = "-7 / 34.2"  # → -0.205
    testfoo = SimpleCalculator()
    result = testfoo.calculation_from_string(x)
    assert result == "-0.205"


def test_minus_before_formula():
    x = "- 6 * 2"  # → -11.98
    testfoo = SimpleCalculator()
    result = testfoo.calculation_from_string(x)
    assert result == "-12"


def test_free_dot_after_numbers():
    x = "2. / 1."  # → 2
    testfoo = SimpleCalculator()
    result = testfoo.calculation_from_string(x)
    assert result == "2"


def test_too_much_operators():
    x = "5 + - 4"  # → ошибка
    testfoo = SimpleCalculator()
    result = testfoo.calculation_from_string(x)
    assert result == "error"


def test_bad_first_symbol():
    x = "*1 + 7"  # → ошибка
    testfoo = SimpleCalculator()
    result = testfoo.calculation_from_string(x)
    assert result == "error"


def test_ignore_parenthesis_in_formula():
    x = "8+ (2)*3"  # 30
    testfoo = SimpleCalculator()
    result = testfoo.calculation_from_string(x)
    assert result == "30"


def test_long_formula():
    x = "3+2-6.5"  # -1.5
    testfoo = SimpleCalculator()
    result = testfoo.calculation_from_string(x)
    assert result == "-1.5"
