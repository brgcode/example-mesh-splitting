from compas.datastructures import Mesh
from compas.geometry import Line, Plane, Frame, Box

box = Box(Frame.worldXY(), 3, 1, 2)
mesh = Mesh.from_shape(box)

line = Line(* box.diagonal)

N = 9
slices = []

a = line.start
for i in range(1, N + 1):
    b = a + line.direction * i * 0.1 * line.length
    plane = Plane(b, line.direction)
    mesh, B = mesh.slice_plane(plane)
    slices.append(B)

slices.append(mesh)
