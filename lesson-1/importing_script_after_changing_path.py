import sys

sys.path.append('lib')

import euclid

origin = (0, 0)
target = (3, 4)
print('Origin:', origin)
print('Target:', target)
print('Distance:', euclid.distance(origin, target))
