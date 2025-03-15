import scipy as sp
import numpy as np

machine_epsilon = np.finfo(float).eps / 2

def hilbert_rel_error(n: int) -> float:
    hilbert = sp.linalg.hilbert(n)
    hinv_n = sp.linalg.inv(hilbert)
    invhilb = sp.linalg.invhilbert(n)

    return sp.linalg.norm(hinv_n - invhilb, ord=2) / sp.linalg.norm(invhilb, ord=2)




if __name__ == '__main__':

    print(" ------------------------------------------------------------------------------------")
    print("| n  | Relative Error | Cond_2(H_n)   | Relative Error/Cond_2(H_n) | Machine Epsilon |")
    print(" ------------------------------------------------------------------------------------")

    for n in range(2, 13):
        rel_error = hilbert_rel_error(n)
        cond_num = np.linalg.cond(sp.linalg.hilbert(n), p=2)

        print("| {:<3}| {:<3.6e}   | {:<13.6e} | {:<16.6e}           | {:<3.6e}    |".
              format(n, rel_error, cond_num, rel_error / cond_num, machine_epsilon))
    print(" ------------------------------------------------------------------------------------")