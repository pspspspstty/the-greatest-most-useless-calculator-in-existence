import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from mpl_toolkits.mplot3d import Axes3D

x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)

class SymbolicMathCalculator:
    """A class for symbolic differentiation, integration, and graphing."""

    def __init__(self):
        """Initialize the calculator."""
        pass

    def derivative(self, expression: str, variables: tuple):
        """Calculate the derivative of an expression with respect to given variables."""
        x, y = symbols(variables)
        try:
            return [diff(expression, var) for var in (x, y)]
        except Exception as e:
            return f"Error in differentiation: {e}"

    def integral(self, expression: str, variables: tuple):
        """Calculate the integral of an expression with respect to given variables."""
        x, y = symbols(variables)
        try:
            return [integrate(expression, var) for var in (x, y)]
        except Exception as e:
            return f"Error in integration: {e}"

    def printIt(self, expression: str):
        init_printing()
        pprint_use_unicode(expression)

    def plot_3d(self, expression: str, variables: tuple, operation: str):
        """
        Plot the 3D graph of the function or its derivatives/antiderivatives.

        Args:
            expression (str): The input function as a string.
            variables (tuple): A tuple containing the variables (e.g., ('x', 'y')).
            operation (str): 'derivative' or 'integral' to specify the operation.
        """
        x, y = symbols(variables)

        # Replace '^' with '**' for Python compatibility
        expression = expression.replace("^", "**")

        # Lambdify the original expression
        original_expr = lambdify((x, y), expression, "numpy")

        if operation == "derivative":
            derivatives = self.derivative(expression, variables)
            derivative_funcs = [lambdify((x, y), d, "numpy") for d in derivatives]
            label = "Derivative"
        elif operation == "integral":
            integrals = self.integral(expression, variables)
            integral_funcs = [lambdify((x, y), i, "numpy") for i in integrals]
            label = "Antiderivative"
        else:
            raise ValueError("Invalid operation. Choose 'derivative' or 'integral'.")

        # Generate data points for 3D plot
        x_vals = np.linspace(-10, 10, 500)
        y_vals = np.linspace(-10, 10, 500)
        X, Y = np.meshgrid(x_vals, y_vals)
        Z = original_expr(X, Y)

        # Create 3D plot
        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
        ax.set_title(f"3D Graph of Function and Its {label}")
        ax.set_xlabel(variables[0])
        ax.set_ylabel(variables[1])
        ax.set_zlabel("f(x, y)")

        plt.show()
