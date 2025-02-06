import random
import math

for _ in range(1000000):
    x = random.uniform(-math.pi/2, math.pi/2)
    y = (1 - math.cos(x))/math.sin(x)
    if y < -2 or y > 2:
        print(x)