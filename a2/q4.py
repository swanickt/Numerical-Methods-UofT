def time_numpy_multiply_experiment(n: int) -> float:
    """Return the time required to multiply two random n x n matrices that
    are stored as NumPy ndarrays and using the NumPy matrix-matrix multiply
    operator.
    """

    # construct the random matrices
    # Students: enter your code here
    A = np.random.random((n, n)) # First random matrix
    B = np.random.random((n, n)) # Second random matrix

    # time the NumPy matrix multiply operation
    # Students: enter your code here

    # time the numpy matrix multiply operation
    start_time = time.perf_counter()
    C = A @ B
    stop_time = time.perf_counter()

    # Students: modify this return statement to return the time required
    #   by the NumPy matrix multiply operation instead of the number 42

    return stop_time - start_time