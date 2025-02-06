import random

### Header for the table ###########################################
print("Approximate fraction of x in [1.5, 2.0) that satisfy 1/(1/x) == x, for the given sample size:")
print(" -------------------------")
print("| Sample Size  | Fraction |")
print(" -------------------------")
####################################################################

def double_reciprocal(num_samples: int) -> int:
    count = 0

    for _ in range(num_samples):
        # generate a random float x between 1.5 and 2.0
        x = random.uniform(1.5, 2.0)
        y = 1 / (1 / x)
        if x == y:
            count += 1

    return count

for i in range(1, 9):
    sample_size = 10 ** i
    num_satisfied = double_reciprocal(sample_size)
    fraction = num_satisfied / sample_size
    print("| {:<12} | {:<8.5f} |".format(sample_size, fraction))

print(" -------------------------") # bottom of the table
