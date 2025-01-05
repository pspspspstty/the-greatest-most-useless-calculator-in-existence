#import libraries
from sympy import *
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor
from .base_operation import Operation

# set transformations when parsing user input
# most noticeably, implicit multiplication is added
# ex: 2x --> 2 * x
transformations = (standard_transformations + (implicit_multiplication_application,) + (convert_xor,))

class LineInt(Operation):
    # ctor for class LineInt
    def __init__(self, fnc: str, cur_x: str, cur_y: str, low_bnd: str, upp_bnd: str):
        self.integrand = fnc
        self.curve_x = cur_x
        self.curve_y = cur_y
        self.low_bound = int(low_bnd)
        self.up_bound = int(upp_bnd)

    # calculates using manual integration
    def calculate(self):
        init_printing()
        t = symbols('t')
        differential = " * sqrt((" + str(diff(self.curve_x, t)) + ")**2 + (" + str(diff(self.curve_y, t)) + ")**2)"

        self.integrand = self.integrand.replace("x", "(" + self.curve_x + ")")
        self.integrand = self.integrand.replace("y", "(" + self.curve_y + ")")
        self.integrand = self.integrand + differential
        print("Your integral, after converting ds to dt: ")
        pprint(Integral(parse_expr(self.integrand, transformations=transformations), (t, self.low_bound, self.up_bound)))

        ans = integrate(parse_expr(self.integrand, transformations=transformations), (t, self.low_bound, self.up_bound))
        print(str(ans) + " --> " + str(ans.evalf()))