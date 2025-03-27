import numpy as np

points = np.linspace(0, np.pi/4, 5)
sin_points = np.sin(points)
p_4 = np.polyfit(points, sin_points, 4)


print(
    " --------------------------------------------------------------------")
print(
    "| Random x    | Sin(x)        | P_4(x)        | abs(Sin(x) - P_4(x)) |")
print(
    " --------------------------------------------------------------------")

for n in range(20):
    x = np.random.uniform(0, np.pi/4)
    sin_x = np.sin(x)
    p4_at_x = np.polyval(p_4, x)

    print(
        "| {:<11.8f} | {:<13.9} | {:<13.9} | {:<20.10e} |".
        format(x, sin_x, p4_at_x, abs(sin_x - p4_at_x)))
print(
    " --------------------------------------------------------------------")

m = 2
error_bound = (1/(4*m))*( (np.pi/(4*(m-1)))**m)

while not (error_bound <= 1e-16):
    m += 1
    error_bound = (1 / (4 * m)) * (np.pi / (4 * (m - 1))) ** m
print(m)
