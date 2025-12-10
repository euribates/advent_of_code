from dataclasses  import dataclass
import math


@dataclass(frozen=True)
class V3:
    x: int = 0
    y: int = 0
    z: int = 0

    def __repr__(self):
        return f'V3({self.x}, {self.y}, {self.z})'

    def distance(self, other) -> float:
        return math.sqrt(
            (self.x - other.x) ** 2
            + (self.y - other.y) ** 2
            + (self.z - other.z) ** 2
            )
