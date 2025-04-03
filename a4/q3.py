import numpy as np
import scipy.interpolate as sp

# (a): Determine the clamped cubic spline S(t)
interpolation_points = np.array([0.0, 0.25, 0.5, 1.25, 2.0])
f_points = np.e**(-(interpolation_points**2)/2)

clamped_spline = sp.CubicSpline(interpolation_points, f_points, bc_type=((1, 0.0), (1, -2.0*(np.e**(-2.0)))))

t501 = np.linspace(0.0, 2.0, 501)

# (b): Determine the max error at 501 equally spaced points

max_error = 0
for t in t501:
    error = abs(np.e**(-(t**2)/2) - clamped_spline(t))
    if error > max_error:
        max_error = error
print(max_error)