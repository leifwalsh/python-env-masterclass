import numby as np

import npgeometry

bases = np.array([3, 5, 8])
heights = np.array([4, 12, 15])
print('Bases:', bases)
print('Heights:', heights)
print('Hypotenuses:', npgeometry.hypotenuse(bases, heights))
