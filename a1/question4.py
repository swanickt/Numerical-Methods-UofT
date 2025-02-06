import math
import random

def f(x: float) -> float:
    return math.tan(x/2)

y = 0.33333333
print( (1 / y) * y)
for _ in range(20):
    x = random.uniform(-math.pi/2, math.pi/2)
    print(x, f(x))