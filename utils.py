def get_user_input():
    """Prompt the user to input a mathematical expression and variable."""
    expression = input("Enter the mathematical expression (e.g., x**2 + 3*x): ").strip()
    variable = input("Enter the variable of differentiation/integration (e.g., x): ").strip()
    return expression, variable