import pytest
from vectors import V2, area


def test_area_zero():
    assert area(V2(0, 0), V2(0, 0)) == 1.0


def test_area_1x1():
    assert area(V2(1, 0), V2(0, 1)) == 4.0


def test_area_2x2():
    assert area(V2(2, 0), V2(0, 2)) == 9.0


def test_area_1x2():
    assert area(V2(1, 1), V2(2, 1)) == 2.0


def test_area_5x5():
    assert area(V2(0, 5), V2(5, 0)) == 36.0

def test_area_3x5():
    assert area(V2(0, 3), V2(5, 0)) == 24.0


def test_area_10x10():
    assert area(V2(1, 1), V2(10, 10)) == 100.0


def test_area_1x10():
    assert area(V2(1, 1), V2(10, 1)) == 10.0


def test_area_negative_3x5():
    assert area(V2(0, -3), V2(-5, 0)) == 24.0


if __name__ == "__main__":
    pytest.main()

