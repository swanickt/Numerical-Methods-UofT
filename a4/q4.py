import math

def g1(x):
    return (x**2 + 2)/3

def g2(x):
    return math.sqrt(3*x - 2)

def g3(x):
    return 3 - (2/x)

def g4(x):
    return (x**2 - 2)/(2*x - 3)

def fixed_point_iteration(g, x0, max_iteration=16):
    """
    Perform fixed point iteration x_{n+1}=g(x_n),
    starting at x0, for max_iteration iterations.
    Prints the relevant table with the iteration number, x_i,
    and the difference |x_i-x_{i-1}|.
    """
    print(" --------------------------------------------------------")
    print("| Iteration  | x_i              | Δ_x = abs(x_i-x_{i-1}) |")
    print(" --------------------------------------------------------")

    x = x0
    print("| 0          | 2.2              |                        |")
    for i in range(1, max_iteration):
        x_new = g(x)
        delta = abs(x_new - x)
        print(f"| {i:<4d}       | {x_new:<13.7}    | {delta:<23.8e}|")

        x = x_new
    print(" --------------------------------------------------------")

if __name__ == '__main__':
    print("Fixed Point Iteration Scheme for g1(x) = (x^2+2)/3:")
    fixed_point_iteration(g1, 2.2)
    print("\nFixed Point Iteration Scheme for g2(x) = sqrt(3x-2):")
    fixed_point_iteration(g2, 2.2)
    print("\nFixed Point Iteration Scheme for g3(x) = 3-(2/x):")
    fixed_point_iteration(g3, 2.2)
    print("\nFixed Point Iteration Scheme for g4(x) = (x^2-2)/(2x-3):")
    fixed_point_iteration(g4, 2.2)