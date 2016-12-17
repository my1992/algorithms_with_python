import numpy as np
import math


def eulidean_distance(a, b):
    if isinstance(a, list) and isinstance(b, list):
        a = np.array(a)
        b = np.array(b)

    return math.sqrt(sum(np.power((a - b), 2)))

