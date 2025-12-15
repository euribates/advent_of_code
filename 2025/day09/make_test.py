import math
import random
from itertools import pairwise

points = []
for angle in range(0, 361, 12):
    rads = angle * math.pi / 180.
    x = math.cos(rads) * random.randrange(120, 190)
    y = math.sin(rads) * random.randrange(120, 190)
    points.append((200 + int(x), 200 + int(y)))
print('Generando test_circle', end=' ')
origin = points[0]
with open('test_circle', 'w') as f:
    for p1, p2 in pairwise(points):
        print(f'{p1[0]},{p1[1]}', file=f)
        if random.random() > 0.5:
            print(f'{p1[0]},{p2[1]}', file=f)
        else:
            print(f'{p2[0]},{p1[1]}', file=f)
    print(f'{p2[0]},{p2[1]}', file=f)
    print(f'{origin[0]},{p2[1]}', file=f)
print('[ok]')
