import scipy as sp
import numpy as np

def pascal_system(n: int):
    """
    Return the nxn Pascal matrix, a random solution vector xstar, and the corresponding
    right-hand-side vector b, in that order.
    """

    A = sp.linalg.pascal(n, kind='symmetric')
    xstar = np.random.rand(n,1)
    b = A @ xstar

    return A, xstar, b

def generate_pascal_table():
    n = 0
    rel_error = 0

    while rel_error <= 1:
        n += 1
        A, xstar, b = pascal_system(n)
        computed_solution = sp.linalg.solve(A, b)

        rel_error = sp.linalg.norm(computed_solution - xstar) / sp.linalg.norm(xstar)
        rel_residual = sp.linalg.norm(b - A @ computed_solution) / sp.linalg.norm(b)
        cond_num = np.linalg.cond(A)
        det = sp.linalg.det(A)

        print("| {:<3}| {:<3.6e}   | {:<13.6e}       | {:<3.4e}   | {:<3.4e}  |".
            format(n, rel_error, rel_residual, cond_num, det))


if __name__ == '__main__':
    print("Testing pascal_system function for n = 3 case:\n")
    A_3, xstar_3, b_3 = pascal_system(3)
    print("Returned matrix A:")
    print(A_3)
    print("Returned vector xstar:")
    print(xstar_3)
    print("Returned vector b:")
    print(b_3)
    print("\n")

    print("Setting up and solving the system Ax = b with scipy.linalg.solve until the normwise\n"
          "relative error in the computed solution is greater than 1:")

    print(" ------------------------------------------------------------------------")
    print("| n  | Relative Error | Relative Residual   | Cond(A)      | det(A)      |")
    print(" ------------------------------------------------------------------------")
    generate_pascal_table()
    print(" ------------------------------------------------------------------------")

