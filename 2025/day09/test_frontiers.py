import pytest
from vectors import V2
from frontiers import Frontiers


def test_simple_frontier():
    f = Frontiers()
    f.add(V2(1,1), V2(10, 1))
    f.add(V2(10,1), V2(10, 10))
    f.add(V2(10,10), V2(1, 10))
    f.add(V2(1, 10), V2(1, 1))
    assert f.is_inside(V2(5, 5)) is True


def test_corners():
    f = Frontiers()
    f.add(V2(1,1), V2(10, 1))
    f.add(V2(10,1), V2(10, 10))
    f.add(V2(10,10), V2(1, 10))
    f.add(V2(1, 10), V2(1, 1))
    assert f.is_inside(V2(0, 1)) is False
    assert f.is_inside(V2(1, 1)) is True
    assert f.is_inside(V2(2, 1)) is True
    assert f.is_inside(V2(9, 1)) is True
    assert f.is_inside(V2(10, 1)) is True
    assert f.is_inside(V2(11, 1)) is False

    assert f.is_inside(V2(1, 0)) is False
    assert f.is_inside(V2(1, 1)) is True
    assert f.is_inside(V2(1, 2)) is True
    assert f.is_inside(V2(1, 9)) is True
    assert f.is_inside(V2(1, 10)) is True
    assert f.is_inside(V2(1, 11)) is False


def test_inside():
    f = Frontiers()
    f.add(V2(1,1), V2(10, 1))
    f.add(V2(10,1), V2(10, 10))
    f.add(V2(10,10), V2(1, 10))
    f.add(V2(1, 10), V2(1, 1))
    for y in range(1, 11):
        for x in range(1, 11):
            assert f.is_inside(V2(x, y)) is True

def test_get_candidates():
    f = Frontiers()
    f.add(V2(1,1), V2(10, 1))
    f.add(V2(10,1), V2(10, 10))
    f.add(V2(10,10), V2(1, 10))
    f.add(V2(1, 10), V2(1, 1))
    assert f.vertexs == [
        V2(1,1),
        V2(10,1),
        V2(10,10),
        V2(1, 10),
        V2(1,1),
        ]

    candidates = set(f.get_candidates())
    assert len(candidates) == 6
    assert candidates == {
        (V2(1, 1), V2(10, 1), 10.0),
        (V2(1, 1), V2(10, 10), 100.0),
        (V2(1, 1), V2(1, 10), 10.0),
        (V2(10, 1), V2(10, 10), 10.0),
        (V2(10, 1), V2(1, 10), 100.0),
        (V2(1, 10), V2(1, 1), 10.0),
        }

if __name__ == "__main__":
    pytest.main()

