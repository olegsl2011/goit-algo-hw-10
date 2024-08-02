import matplotlib.pyplot as plt
import numpy as np

from scipy.integrate import quad


def plot_integral(f, a, b, n=1000):
    x = np.linspace(a - 1, b + 1, n)
    y = f(x)

    fig, ax = plt.subplots()

    ax.plot(x, y, 'r', linewidth=2)

    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title(f'Integral of f(x) between {a} and {b}')
    plt.grid()
    plt.show()


def numeric_integral(f, a, b):
    result, error = quad(f, a, b)
    return result


def monte_carlo_integral(f, a, b, max_y, num_samples=10000):
    x_samples = np.random.uniform(a, b, num_samples)
    y_samples = np.random.uniform(0, max_y, num_samples)

    under_curve_samples = np.sum(y_samples <= f(x_samples))

    return (b - a) * under_curve_samples / num_samples


def main():
    def f(x):
        return 1 / (1 + x ** 2)

    a = -3
    b = 3

    plot_integral(f, a, b)

    print(f"Numeric integral: {numeric_integral(f, a, b)}")

    max_y = 1

    print(f"Monte Carlo integral (100 samples): {monte_carlo_integral(f, a, b, max_y, num_samples=100)}")

    print(f"Monte Carlo integral (10000 samples): {monte_carlo_integral(f, a, b, max_y, num_samples=10000)}")
    
    print(f"Monte Carlo integral (1000000 samples): {monte_carlo_integral(f, a, b, max_y, num_samples=1000000)}")


if __name__ == "__main__":
    main()
