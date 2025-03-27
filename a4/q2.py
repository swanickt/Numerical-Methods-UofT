import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as sp

def absolute_value_polynomial_interpolation(m: int) -> None:
    interpolation_points = np.linspace(-1, 1, m)
    abs_points = abs(interpolation_points)
    p = np.polyfit(interpolation_points, abs_points, deg=m-1)

    # Plotting f(t)=|t| and p(t)
    t1001 = np.linspace(-1, 1, 1001)
    tplot = np.hstack([interpolation_points, t1001])
    tplot.sort()

    fig, axs = plt.subplots(2, 1, constrained_layout=True)
    fig.suptitle(f'Visualizing the degree {m-1} polynomial interpolant of |t|',
                 fontsize=12)

    axs[0].plot(interpolation_points, abs_points, 'o', label='data')
    axs[0].plot(tplot, abs(tplot), '-', label='|t|')
    axs[0].plot(tplot, np.polyval(p, tplot), '--', label=f'p(t)')
    axs[0].set_xlabel('t')
    axs[0].set_ylabel('y')
    axs[0].legend()

    # plot the error |f(t) - p(t)| vs. t
    axs[1].plot(tplot, np.abs(abs(tplot) - np.polyval(p, tplot)), '-',
                label=f'||t| - p(t)|')
    axs[1].set_yscale('log')
    axs[1].set_xlabel('t')
    axs[1].set_ylabel('||t| - p(t)|')
    axs[1].legend()

    plt.show()

def absolute_value_cubic_spline_interpolation(m: int) -> None:
    interpolation_points = np.linspace(-1, 1, m)
    abs_points = abs(interpolation_points)
    cs = sp.CubicSpline(interpolation_points, abs_points)

    # Plotting f(t)=|t| and cs(t)
    t1001 = np.linspace(-1, 1, 1001)
    tplot = np.hstack([interpolation_points, t1001])
    tplot.sort()

    fig, axs = plt.subplots(2, 1, constrained_layout=True)
    fig.suptitle('Visualizing a cubic spline interpolant of |t|',
                 fontsize=12)

    axs[0].plot(interpolation_points, abs_points, 'o', label='data')
    axs[0].plot(tplot, abs(tplot), '-', label='|t|')
    axs[0].plot(tplot, cs(tplot), '--', label='cubic_spline(t)')
    axs[0].set_xlabel('t')
    axs[0].set_ylabel('y')
    axs[0].legend()

    # plot the error |f(t) - cs(t)| vs. t
    axs[1].plot(tplot, np.abs(abs(tplot) - cs(tplot)), '-',
                label='||t| - cs(t)|')
    axs[1].set_yscale('log')
    axs[1].set_xlabel('t')
    axs[1].set_ylabel('||t| - cs(t)|')
    axs[1].legend()

    plt.show()

absolute_value_polynomial_interpolation(5)
absolute_value_polynomial_interpolation(11)
absolute_value_polynomial_interpolation(21)

absolute_value_cubic_spline_interpolation(5)
absolute_value_cubic_spline_interpolation(11)
absolute_value_cubic_spline_interpolation(21)