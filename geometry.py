from math import sqrt

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return sqrt(dx*dx + dy*dy)

print(distance (0,0, 3,4))
