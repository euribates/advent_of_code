#!/usr/bin/env python

from collections import defaultdict

import pytest

from machines import Machine


def test_sample_one():
    m = Machine('[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}')
    assert m.is_ready() is False
    assert m.target == [False, True, True, False]
    assert m.leds == [False, False, False, False]
    m = m.press_button(4)
    assert m.is_ready() is False
    assert m.leds == [True, False, True, False]
    m = m.press_button(5)
    assert m.is_ready() is True
    assert m.leds == [False, True, True, False]
    

def test_label():
    m = Machine('[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}')
    assert m.label == '....'
    m = m.press_button(0)
    assert m.label == '...#'
    m = m.press_button(2)
    assert m.label == '..##'


def test_frist_sample_ready():
    m = Machine('[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}')
    assert m.label == '....'
    assert m.is_ready() is False
    m = m.press_button(0)
    assert m.label == '...#'
    assert m.is_ready() is False
    m = m.press_button(1)
    assert m.label == '.#..'
    assert m.is_ready() is False
    m = m.press_button(2)
    assert m.label == '.##.'
    assert m.is_ready() is True




def test_sample_two():
    m = Machine('[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}')
    assert m.is_ready() is False
    assert m.target == [False, False, False, True, False]
    m = m.press_button(2)
    m = m.press_button(3)
    m = m.press_button(4)
    assert m.is_ready() is True


def test_sample_three():
    m = Machine('[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}')
    assert m.is_ready() is False
    m = m.press_button(1)
    assert m.is_ready() is False
    m = m.press_button(2)
    assert m.is_ready() is True
    

def test_buttons_equal_number_of_voltages():
    from core import load_input
    for m in load_input('input'):
        assert m.num_leds == len(m.joltages)


def test_is_over_joltage():
    m = Machine('[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}')
    assert m.is_over_joltage([0, 2, 0, 2]) is False
    assert m.is_over_joltage([0, 5, 0, 5]) is False
    assert m.is_over_joltage([0, 6, 0, 6]) is True


def test_get_commands():
    m = Machine('[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}')
    expected = {
        (3,): [
            (0, 0, 0, 1),
            (0, 0, 0, 2),
            (0, 0, 0, 3),
            (0, 0, 0, 4),
            (0, 0, 0, 5),
            (0, 0, 0, 6),
            (0, 0, 0, 7),
            ],
        (1, 3): [
            (0, 1, 0, 1),
            (0, 2, 0, 2),
            (0, 3, 0, 3),
            (0, 4, 0, 4),
            (0, 5, 0, 5),
            ],
        (2,): [
            (0, 0, 1, 0),
            (0, 0, 2, 0),
            (0, 0, 3, 0),
            (0, 0, 4, 0),
            ],
        (2, 3): [
            (0, 0, 1, 1),
            (0, 0, 2, 2),
            (0, 0, 3, 3),
            (0, 0, 4, 4),
            ],
        (0, 2): [
            (1, 0, 1, 0),
            (2, 0, 2, 0),
            (3, 0, 3, 0),
            ],
        (0, 1): [
            (1, 1, 0, 0),
            (2, 2, 0, 0),
            (3, 3, 0, 0),
            ],
        }
    commands = defaultdict(list)
    for button, cmds in m.get_commands():
        commands[button].append(cmds)
    assert commands == expected


def test_part_2_sample_1():
    m = Machine('[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}')
    m.apply_command([0, 0, 0, 1]) # (3) * 1
    m.apply_command([0, 3, 0, 3]) # (1, 3) * 3
    m.apply_command([0, 0, 3, 3]) # (2, 3) * 3
    m.apply_command([1, 0, 1, 0]) # (0, 2) * 1
    m.apply_command([2, 2, 0, 0]) # (0, 1) * 2
    assert m.is_working() is True


if __name__ == '__main__':
    pytest.main()
