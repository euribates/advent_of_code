from dataclasses  import dataclass
import math


@dataclass(frozen=True)
class V2:
    x: float = 0.0
    y: float = 0.0

    def __repr__(self):
        return f'V2({self.x}, {self.y})'

    def distance(self, other) -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __mul__(self, factor):
        return V2(self.x * factor, self.y * factor)


def area(p1: V2, p2: V2) -> int|float:
    width = (p1.x - p2.x if p1.x > p2.x else p2.x - p1.x) + 1
    height = (p1.y - p2.y if p1.y > p2.y else p2.y - p1.y) + 1
    return width  * height

