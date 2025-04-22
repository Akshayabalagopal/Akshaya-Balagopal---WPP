import numpy as np
import random
import matplotlib.pyplot as plt

#polynomial
def f(x, coefficients):
    return sum(c * x**i for i, c in enumerate(coefficients))

# Check if the function has opposite signs at two points, implying a root exists between them
def has_opposite_signs(f, a, b, coefficients):
    return f(a, coefficients) * f(b, coefficients) < 0

# Bisection method
def bisection_method(f, a, b, coefficients, tolerance=1e-6, max_iterations=100):
    updates = []  # To store midpoints for plotting
    iterations = 0
    root = None  # This will store the final root value

    # Continue while the interval is large enough and we haven't reached the max iterations
    while (b - a) / 2 > tolerance and iterations < max_iterations:
        midpoint = (a + b) / 2
        updates.append(midpoint)

        # Check if midpoint is the root
        if f(midpoint, coefficients) == 0:
            root = midpoint
            break
        
        # Narrow down the interval based on the sign of the function at the midpoint
        if has_opposite_signs(f, a, midpoint, coefficients):
            b = midpoint
        else:
            a = midpoint
        
        iterations += 1
    
    # If we exit the loop without finding the exact root, use the last midpoint as the root
    if root is None:
        root = (a + b) / 2

    return updates, root

# Randomly find an initial interval [a, b] such that f(a) * f(b) < 0
def find_initial_interval(f, coefficients, lower=-10, upper=10):
    a = random.uniform(lower, upper)
    b = random.uniform(lower, upper)
    # Keep generating until f(a) and f(b) have opposite signs
    while f(a, coefficients) * f(b, coefficients) > 0:  
        a = random.uniform(lower, upper)
        b = random.uniform(lower, upper)
    return a, b

if __name__ == "__main__":
    try:
        coefficients = list(map(float, input("Enter the coefficients of the polynomial (e.g., 1 -4 2 -1 for x^3 - 4x^2 + 2x - 1): ").split()))
        tolerance = float(input("Enter the tolerance for the root (e.g., 1e-6): "))
        
        # Find a random initial interval
        a, b = find_initial_interval(f, coefficients)
        print(f"Initial interval: [{a}, {b}]")

        # Apply the bisection method
        updates, root = bisection_method(f, a, b, coefficients, tolerance)
        
        # Print the root and number of iterations
        print(f"Root found: {root}")
        print(f"Number of iterations: {len(updates)}")

        # Plot the bisection process
        x_vals = np.linspace(a - 2, b + 2, 400)
        y_vals = f(x_vals, coefficients)
        plt.plot(x_vals, y_vals, label="f(x)", color="blue")
        plt.axhline(0, color='black',linewidth=1)

        # Plot the midpoints found by the bisection method
        updates = np.array(updates)
        plt.scatter(updates, f(updates, coefficients), color="red", zorder=5, label="Midpoints")
        
        # Add labels and a title
        plt.title("Bisection Method Root Finding Process")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.legend()
        plt.grid(True)
        plt.show()

    except ValueError:
        print("Invalid input. Please enter valid numbers for coefficients and tolerance.")



