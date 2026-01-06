from dataclasses  import dataclass
import math


@dataclass(frozen=True)
class V2:
    x: float = 0.0
    y: float = 0.0

    def __repr__(self):
        return f'V2({self.x}, {self.y})'

    def distance(self, other) -> float:
        return math.sqrt(
              (self.x - other.x) ** 2
            + (self.y - other.y) ** 2
            )

    def __add__(self, other):
        return V2(
            self.x + other.x,
            self.y + other.y,
            )

    def __mul__(self, factor):
        return V2(self.x * factor, self.y * factor)


def area(p1: V2, p2: V2) -> int|float:
    width = abs(p2.x - p1.x) + 1
    height = abs(p2.y - p1.y) + 1
    return width  * height


@dataclass(frozen=True)
class V3:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    def __repr__(self):
        return f'V3({self.x}, {self.y}, {self.z})'

    def distance(self, other) -> float:
        return math.sqrt(
            (self.x - other.x) ** 2
          + (self.y - other.y) ** 2
          + (self.z - other.z) ** 2
          )

    def __add__(self, other: 'V3'):
        return V3(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
            )

    def __mul__(self, factor):
        return V3(self.x * factor, self.y * factor, self.z * factor)

    def rotate_on_y(self, angle):
        s = math.sin(angle)
        c = math.cos(angle)
        return V3(
            x=self.x * c - self.z * s,
            y=self.y,
            z=self.x * s + self.z * c,
            )
