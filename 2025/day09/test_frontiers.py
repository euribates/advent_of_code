import pytest
from vectors import V2
from frontiers import FilledBoxes


def test_simple_box_bounderies():
    box = FilledBoxes(4, 5)
    assert V2(3, 4) not in box
    assert V2(4, 4) not in box
    assert V2(5, 4) not in box
    assert V2(3, 5) not in box
    assert V2(4, 5) in box
    assert V2(5, 5) not in box
    assert V2(3, 6) not in box
    assert V2(4, 6) not in box
    assert V2(5, 6) not in box

def test_simple_box_expand_right():
    box = FilledBoxes(4, 5)
    box = box.expand_right()
    assert V2(3, 4) not in box
    assert V2(4, 4) not in box
    assert V2(5, 4) not in box
    assert V2(3, 5) not in box
    assert V2(4, 5) in box
    assert V2(5, 5) in box
    assert V2(3, 6) not in box
    assert V2(4, 6) not in box
    assert V2(5, 6) not in box

def test_simple_box_expand_left():
    box = FilledBoxes(4, 5)
    box = box.expand_left()
    assert V2(3, 4) not in box
    assert V2(4, 4) not in box
    assert V2(5, 4) not in box
    assert V2(3, 5) in box
    assert V2(4, 5) in box
    assert V2(5, 5) not in box
    assert V2(3, 6) not in box
    assert V2(4, 6) not in box
    assert V2(5, 6) not in box

def test_simple_box_area():
    box = FilledBoxes(4, 5)
    assert box.area == 1
    box = box.expand_left()
    assert box.area == 2
    box = box.expand_right()
    assert box.area == 3
    box = box.expand_down()
    assert box.area == 6
    box = box.expand_up()
    assert box.area == 9

def test_box_full_expand():
    box = (
        FilledBoxes(4, 5)
        .expand_left()
        .expand_right()
        .expand_down()
        .expand_up()
        )
    assert box.area == 9
    assert V2(3, 4) in box
    assert V2(4, 4) in box
    assert V2(5, 4) in box
    assert V2(3, 5) in box
    assert V2(4, 5) in box
    assert V2(5, 5) in box
    assert V2(3, 6) in box
    assert V2(4, 6) in box
    assert V2(5, 6) in box



if __name__ == "__main__":
    pytest.main()

