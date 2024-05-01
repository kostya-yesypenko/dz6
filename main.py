import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 2*x**3 - 3*x**2 - 60*x + 170

def half_interval_method_verbose(f, a, b, tol):
    iterations = []
    while abs(b - a) > tol:
        mid = (a + b) / 2
        if f(mid - tol) < f(mid + tol):
            b = mid
        else:
            a = mid
        iterations.append((a, b, (a + b) / 2, abs(b - a)))
    return (a + b) / 2, iterations

def dichotomy_method_verbose(f, a, b, tol):
    iterations = []
    ratio = 0.618
    while abs(b - a) > tol:
        x1 = b - ratio * (b - a)
        x2 = a + ratio * (b - a)
        if f(x1) < f(x2):
            b = x2
        else:
            a = x1
        iterations.append((a, b, (a + b) / 2, abs(b - a)))
    return (a + b) / 2, iterations

# Виклик функцій для знаходження мінімуму за допомогою обох методів
optimal_x_half, iterations_half = half_interval_method_verbose(f, 0, 10, 0.01)
optimal_x_dichotomy, iterations_dichotomy = dichotomy_method_verbose(f, 0, 10, 0.01)

# Вивід результатів
print("Метод половинного ділення:")
print("Оптимальне значення x:", optimal_x_half)
print("Значення функції при оптимальному x:", f(optimal_x_half))

print("\nМетод дихотомії:")
print("Оптимальне значення x:", optimal_x_dichotomy)
print("Значення функції при оптимальному x:", f(optimal_x_dichotomy))

# Побудова таблиць ітерацій
def print_iterations_table(iterations, method):
    print("\nТаблиця ітерацій для", method)
    print("k |  ak  |  bk  |  xk(c)  |  |bk - ak|")
    print("---------------------------------------")
    for k, (ak, bk, xk, bk_ak) in enumerate(iterations):
        print("{:2d} | {:.2f} | {:.2f} | {:.2f} | {:.2f}".format(k+1, ak, bk, xk, bk_ak))

print_iterations_table(iterations_half, "методу половинного ділення")
print_iterations_table(iterations_dichotomy, "методу дихотомії")


x = np.linspace(0, 10, 400)
y = f(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Графік цільової функції')
plt.grid(True)
plt.show()
