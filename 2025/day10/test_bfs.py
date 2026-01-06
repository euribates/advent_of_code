#!/usr/bin/env python

import pytest

from machines import Machine
from part_01 import bfs


def test_part_1_sample_one():
    m = Machine('[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}')
    assert bfs(m) == 2

if __name__ == '__main__':
    pytest.main()
