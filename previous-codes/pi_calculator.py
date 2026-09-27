import numpy as np
import sys

# markov calculator
# define the quadrant
val_range = [0,1]
# number of points to sample from the quadrant
num_pts = int(sys.argv[1])
# sample points uniformly at random
data = np.random.uniform(low=val_range[0], \
                         high=val_range[1], \
                         size=(num_pts, 2))
# computing distances from the origin
distance = np.sum(data*data, axis=1)
# count now
distance[distance <= 1] = 1
distance[distance > 1] = 0
# print 4*ratio
pi = 4*np.sum(distance) / num_pts
print("value of pi:", pi)