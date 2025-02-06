# Python 3 program to generate results for Computer Problem 1.1 in the 
# Heath text (pg. 44).

import math

# Compute and print Sterling's approximation to n! for n = 1,2,3,...,10

### Header for the table ###########################################
print(" ------------------------------------------------------------")
print("|  n |       n!  |       approximation |  abs err |  rel err |")
print(" ------------------------------------------------------------")
####################################################################

for n in range(1, 11):

    true_value = math.factorial(n)
    sterling_approximation = math.sqrt(math.tau * n) * pow(n / math.e, n)
    abs_error = abs(sterling_approximation - true_value)
    rel_error = abs_error / abs(true_value)
    # print(n, true_value, sterling_approximation, abs_error, rel_error)

    print("| {:>2} | {:>9} | {:>19.13e} | {:>8.2e} | {:>8.2e} |".format(n, true_value, sterling_approximation,
                                                                abs_error, rel_error))
    # {:>8.2e} - nothing on LHS of : means pad with " "
    #          - >8 means right align and pad leftover space (up to 8 places) with " "
    #          - .2e means 2 significant digits (after decimal) of accuracy in scientific notation
    #          - (i.e. 7.79e-02 = 7.79x10^{-2} )

print(" ------------------------------------------------------------")

### (produced by ChatGPT) ###

"""Once you have an easy to read set of results, reflect on them and thing about your answers to the
following questions:
1. Why report only a few significant figures for the errors?
(a SIGNIFICANT FIGURE is: each of the digits of a number that are used to express it to the required degree of accuracy, 
starting from the first nonzero digit. ex) the number of significant figures in 0.042 is two, since this can be written as
42 x 10^{-2} )

2. Does the absolute error grow or shrink as n increases?
3. Does the relative error grow or shrink as n increases?
4. Would you recommend using absolute error or relative error when evaluating the suitablity of using
Stirling’s approximation to n!?"""

""" 1.) Reporting only a few significant figures for the errors is sufficient because the errors themselves are approximations. 
Including more significant figures does not provide additional meaningful precision but may mislead the reader into thinking 
the error estimate is more accurate than it is.

Additionally, using a small number of significant figures makes the results easier to interpret and avoids unnecessary detail, 
especially when comparing values."""

""" 2.) From the results, the absolute error grows as n increases. This is because the factorial n! grows extremely rapidly, 
and Stirling's approximation, while good, deviates further in absolute terms for larger n. """

""" 3.) The relative error shrinks as n increases. Despite the absolute error growing, the factorial n!
grows much faster, so the ratio of the error to n! becomes smaller. """

""" 4.) Relative error is the more appropriate metric for evaluating the suitability of Stirling's approximation because it provides 
a normalized measure of error relative to the size of n!. Absolute error alone can be misleading since it grows as 
n increases, but this growth does not necessarily indicate poor approximation; it’s a result of the factorial’s rapid growth.
Relative error accounts for the scale of the factorial and shows that Stirling's approximation becomes increasingly accurate (in relative terms) as 
n increases, which is a more meaningful evaluation of its effectiveness."""