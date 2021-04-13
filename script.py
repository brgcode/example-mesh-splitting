from compas.datastructures import Mesh
from compas.geometry import Line, Plane, Frame, Box, Translation
from compas.utilities import i_to_rgb

from compas_view2.app import App

# ==============================================================================
# Box mesh
# ==============================================================================

box = Box(Frame.worldXY(), 3, 1, 2)
mesh = Mesh.from_shape(box)

# ==============================================================================
# Diagonal slice direction
# ==============================================================================

line = Line(* box.diagonal)

# ==============================================================================
# Slices
# ==============================================================================

N = 9
slices = []

a = line.start
for i in range(1, N + 1):
    b = a + line.direction * i * 0.1 * line.length
    plane = Plane(b, line.direction)
    mesh, B = mesh.slice_plane(plane)
    slices.append(B)

slices.append(mesh)

# ==============================================================================
# Exploded viz
# ==============================================================================

viewer = App()

for i, mesh in enumerate(slices):
    T = Translation.from_vector(line.direction * i * 0.05 * line.length)
    viewer.add(mesh.transformed(T), facecolor=i_to_rgb(i / N, normalize=True))

viewer.run()
