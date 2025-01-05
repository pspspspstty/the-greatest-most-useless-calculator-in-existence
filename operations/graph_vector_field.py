# import libraries
from sympy import *
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor
from .base_operation import Operation
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# set transformations when parsing user input
# most noticeably, implicit multiplication is added
# ex: 2x --> 2 * x
transformations = (standard_transformations + (implicit_multiplication_application,) + (convert_xor,))

class GraphVF(Operation):
    # constructor  for class GraphVF
    def __init__(self, xinput: str, yinput: str, zinput: str):
        x, y, z = symbols('x y z')

        # sets the respective components to the user input
        # the user input is parsed, and then is "lambdified" to be compatible with numpy
        self.x_component = lambdify((x, y, z), parse_expr(xinput, transformations=transformations), "numpy")
        self.y_component = lambdify((x, y, z), parse_expr(yinput, transformations=transformations), "numpy")
        self.z_component = lambdify((x, y, z), parse_expr(zinput, transformations=transformations), "numpy")

    # calculates and plots the vector field
    def calculate(self):
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        # create 3d grid
        x, y, z = np.meshgrid(np.arange(-4, 4, 1),
                              np.arange(-4, 4, 1),
                              np.arange(-4, 4, 1))

        # creates vector components
        u = self.x_component(x, y, z)
        v = self.y_component(x, y, z)
        w = self.z_component(x, y, z)

        # computes magnitude of a vector
        # ||vector|| = sqrt(u^2 + v^2 + w^2)
        magnitude = np.sqrt(u**2 + v**2 + w**2)

        # normalize the magnitude set so it's not just one color the whole time
        norm = plt.Normalize(vmin=np.min(magnitude), vmax=np.max(magnitude))

        # sets magnitude gradient color
        cmap = matplotlib.cm.get_cmap('viridis')

        # creates an array of RGBA colors based on the normalized magnitudes
        rgba_colors = cmap(norm(magnitude))

        # ensures the colors have the correct "shape" for the quiver function
        # basically reshapes it so that it fits and doesn't throw an error
        rgba_colors = rgba_colors.reshape(-1, 4)

        # creates the vector field
        ax.quiver(x, y, z, u, v, w, length=1, normalize=True, color=rgba_colors)

        # plot the x, y, and z axes
        ax.plot([0, 0], [0, 0], [-1, 1], color='r', linewidth=2)  # X axis (red line)
        ax.plot([0, 0], [-1, 1], [0, 0], color='g', linewidth=2)  # Y axis (green line)
        ax.plot([-1, 1], [0, 0], [0, 0], color='b', linewidth=2)  # Z axis (blue line)

        # adds color bar for references
        cbar = plt.colorbar(matplotlib.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax)
        cbar.set_label('Magnitude')

        # adds grid (not really noticeable)
        ax.grid(True)

        # displays the vector field
        plt.show()