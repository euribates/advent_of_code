import pytest

from part_02 import unverticalize
from part_02 import batch
from part_02 import get_cols_widths


def test_get_cols_widths():
    sample = '123  43      123546 12 1 2  '
    expected = [5, 8, 7, 3, 2, 3]
    assert get_cols_widths(sample) == expected


def test_get_cols_widths_no_margin_at_end():
    sample = '123  43      123546 12 1 24578'
    expected = [5, 8, 7, 3, 2, 5]
    assert get_cols_widths(sample) == expected


def test_unverticalizea_col_4():
    assert set(unverticalize(['64 ', '23 ', '314'])) == {4, 431, 623}


def test_unverticalizea_col_3():
    assert set(unverticalize([' 51', '387', '215'])) == {175, 581, 32}


def test_unverticalizea_col_2():
    assert set(unverticalize(['328', '64 ', '98 '])) == {8, 248, 369}


def test_unverticalizea_col_1():
    assert set(unverticalize(['123', ' 45', '  6'])) == {356, 24, 1}


def test_batch_line_1():
    assert list(batch('123 328  51 64 ', 3)) == ['123', '328', ' 51', '64 '] 


def test_batch_line_2():
    assert list(batch(' 45 64  387 23 ', 3)) == [' 45', '64 ', '387', '23 '] 


def test_batch_line_3():
    assert list(batch('  6 98  215 314', 3)) == ['  6', '98 ', '215', '314'] 



if __name__ == "__main__":
    pytest.main()
