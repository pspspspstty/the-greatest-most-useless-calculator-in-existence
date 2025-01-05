from sympy import symbols, sympify, SympifyError
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor
from operations import *

transformations = (standard_transformations + (implicit_multiplication_application,) + (convert_xor,))

class Menu:
    def __init__(self):
        pass

    def display_menu(self):
        """Displays menu"""
        menu = (
            "1. Line integral of a vector-valued function\n"
            "2. Line integral of a vector field \033[93m( work integral )\033[0m\n"
            "3. Surface integral over a surface\n"
            "4. Surface integral of a vector field \033[93m( flux integral )\033[0m\n"
            "5. Graph a vector field\n"
            "\033[93m\033[1mSelect an operation: \033[0m"
        )
        return menu

    def get_operation(self):
        while True:
            try:
                operation = input(self.display_menu()).strip()
                if not operation:
                    print("\033[31mNo input detected. Enter a number between 1 and 5.\033[0m")
                if 0 < int(operation) <= 5:
                    return operation
                else:
                    print("\033[31mInvalid operation. Enter a number between 1 and 5.\033[0m")
                    continue
            except ValueError:
                print("\033[31mInvalid input. Enter a number between 1 and 5.\033[0m")
                continue

    def check_for_var(self, prompt: str, variables):
        while True:
            user_input = input(prompt).strip()
            try:
                expr = parse_expr(user_input, transformations=transformations)
                if not expr.free_symbols.issubset(variables):
                    raise ValueError()
                return user_input
            except (TypeError, ValueError):
                print("\033[31mInvalid input. Use correct variables.\033[0m")

    def check_bounds_for_var(self, prompt: str):
        while True:
            user_input = input(prompt).strip()
            try:
                expr = parse_expr(user_input, transformations=transformations)
                if expr.free_symbols:
                    raise ValueError("Use numeric values without variables.")
                if not expr.is_number:
                    raise ValueError("Use a valid number.")
                return user_input
            except (TypeError, ValueError) as e:
                print(f"\033[31mInvalid input. {e}\033[0m")

    def validate_bounds(self, low_bound, up_bound):
        while True:
            low_bnd = self.check_bounds_for_var(low_bound)
            upp_bnd = self.check_bounds_for_var(up_bound)
            try:
                low = float(low_bnd)
                up = float(upp_bnd)
                if low < up:
                    return low_bnd, upp_bnd
                else:
                    raise ValueError("Invalid bounds.")
            except (TypeError, ValueError) as e:
                print(f"\033[31mInvalid input. {e}\033[0m")

    def create_line_int(self):
        print("Line integral selected")

        t = symbols('t')
        x, y = symbols('x y')

        fnc = self.check_for_var("Enter the \033[93mintegrand\033[0m in terms of x and y ( ex: xy + x ): ", {x, y})
        cur_x = self.check_for_var("Enter the \033[93mx component\033[0m of the parameterized curve in terms of t ( ex: t^2 + 1 ): ", {t})
        cur_y = self.check_for_var("Enter the \033[93my component\033[0m of the parameterized curve in terms of t ( ex: t^2 + 1 ): ", {t})
        low_bnd, upp_bnd = self.validate_bounds("Enter the \033[93mlower bound\033[0m of t ( ex: 0 ): ", "Enter the \033[93mupper bound\033[0m of t ( ex: 2 ): ")

        return line_integral.LineInt(fnc, cur_x, cur_y, low_bnd, upp_bnd)

    def create_work_int(self):
        print("Work integral selected")
        return work_integral.WorkInt()

    def create_surf_int(self):
        print("Surface integral selected")
        return surface_integral.SurfInt()

    def create_flux_int(self):
        print("Flux integral selected")
        return flux_integral.FluxInt()

    def create_vf(self):
        print("Vector Field selected")

        x, y, z = symbols('x y z')

        x_comp = self.check_for_var("Enter the \033[93mx component\033[0m: ", {x,y,z})
        y_comp = self.check_for_var("Enter the \033[93my component\033[0m: ", {x,y,z})
        z_comp = self.check_for_var("Enter the \033[93mz component\033[0m: ", {x,y,z})

        return graph_vector_field.GraphVF(x_comp, y_comp, z_comp)

    def select_operation(self, op: int):
        match op:
            case 1:
                return self.create_line_int()
            case 2:
                return self.create_work_int()
            case 3:
                return self.create_surf_int()
            case 4:
                return self.create_flux_int()
            case 5:
                return self.create_vf()