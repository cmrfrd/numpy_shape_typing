from typing import Literal

import numpy as np
from numpy.typing import NDArray

from numpy_shape_typing.add import add
from numpy_shape_typing.dot import dot
from numpy_shape_typing.rand import rand_normal_matrix
from numpy_shape_typing.ravel import ravel
from numpy_shape_typing.types import ONE, T1, T2, GenericDType, Shape1D, Shape2D


def Linear(
    A: NDArray[Shape2D[T1, T2], GenericDType],
    x: NDArray[Shape2D[T2, ONE], GenericDType],
    b: NDArray[Shape2D[T1, ONE], GenericDType],
) -> NDArray[Shape1D[T1], GenericDType]:
    Ax = dot(A, x)
    Axb = add(Ax, b)
    return ravel(Axb)


IN_DIM = Literal[3]
in_dim: IN_DIM = 3

OUT_DIM = Literal[4]
out_dim: OUT_DIM = 4

A: NDArray[Shape2D[OUT_DIM, IN_DIM], np.float64] = rand_normal_matrix((out_dim, in_dim))
x: NDArray[Shape2D[IN_DIM, ONE], np.float64] = rand_normal_matrix((in_dim, 1))
b: NDArray[Shape2D[OUT_DIM, ONE], np.float64] = rand_normal_matrix((out_dim, 1))
y: NDArray[Shape1D[OUT_DIM], np.float64] = Linear(A, x, b)

# y = Ax + b
print("A:")
print(A.astype(int))
print("x:")
print(x.astype(int))
print("b:")
print(b.astype(int))
print("y:")
print(y.astype(int))
