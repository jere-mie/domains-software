import numpy as np

# angle between two vectors
def angle(a, b):
    c = np.dot(a,b)/np.linalg.norm(a)/np.linalg.norm(b)
    return np.arccos(np.clip(c, -1, 1))
