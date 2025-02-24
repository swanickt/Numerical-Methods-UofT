import numpy as np
import matplotlib
print(np.__version__)
print(matplotlib.__version__)

x = np.array([(-1)**(i+1) for i in range(10)], dtype=float)
print(x.dtype)
