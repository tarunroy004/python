import numpy as np
from scipy.optimize import minimize
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Define a simple quadratic function for optimization
def func(x):
    return (x - 3) ** 2 + 2

# Optimization: Find the minimum of the function
result = minimize(func, x0=0)
print("Optimization Result:")
print(f"Minimum value of the function: {result.fun}")
print(f"At x: {result.x[0]}")

# Define a simple function for integration
def integrand(x):
    return np.exp(-x**2)

# Integration: Calculate the integral of the function from 0 to 1
integral_result, error = quad(integrand, 0, 1)
print("\nIntegration Result:")
print(f"Integral of exp(-x^2) from 0 to 1: {integral_result}")
print(f"Estimated error: {error}")

# Visualization: Plot the function and its minimum
x_vals = np.linspace(-2, 8, 400)
y_vals = func(x_vals)

plt.plot(x_vals, y_vals, label='(x-3)^2 + 2')
plt.scatter(result.x, result.fun, color='red', zorder=5, label='Minimum')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Optimization of (x-3)^2 + 2')
plt.legend()
plt.grid(True)
plt.show()
