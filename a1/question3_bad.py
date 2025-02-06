import math
from math import sqrt

### Header for the table ###########################################
print(" --------------------------------------------")
print("| n  | p_n                  | Relative Error |")
print(" --------------------------------------------")
####################################################################

power_of_two = 2 # will use this variable to compute 2**n

def relative_error(perimeter_n):
    """
    Return the relative error of the approximation for math.pi given by p_n.
    """
    return abs(perimeter_n - math.pi) / abs(math.pi)

# will hold tuples of the form (n, p_n, relative error)
results = [(2, 2 * sqrt(2), relative_error(2 * sqrt(2)))]

for n in range(3, 41):
    power_of_two = 2 * power_of_two
    previous_perimeter = results[n - 3][1]
    p_n = power_of_two * sqrt(2 * (1 - sqrt(1 - (previous_perimeter / power_of_two) ** 2)))
    results.append((n, p_n, relative_error(p_n)))

# print(n, p_n, relative error)
for n in range(3, 41):
    print("| {:<2} | {:<19.14f} | {:<15.2e} |".format(n, results[n - 2][1], results[n - 2][2]))

print(" --------------------------------------------") # bottom of the table