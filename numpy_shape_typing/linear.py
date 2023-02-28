from typing import Literal

import numpy as np
from numpy.typing import NDArray

from numpy_shape_typing.fake_alegebraic import ONE, T1, T2, GenericDType, Shape1D, Shape2D, ShapeNDType
from numpy_shape_typing.matadd import matadd
from numpy_shape_typing.matmul import matmul
from numpy_shape_typing.ravel import ravel


def rand_binary_matrix(shape: ShapeNDType) -> NDArray[ShapeNDType, np.bool_]:
    """Return a random binary matrix."""
    return np.random.randint(low=0, high=2, size=shape, dtype=bool)


def rand_normal_matrix(shape: ShapeNDType) -> NDArray[ShapeNDType, np.float64]:
    """Return a random ND normal matrix."""
    return np.random.standard_normal(size=shape)


def Linear(
    A: NDArray[Shape2D[T1, T2], GenericDType],
    x: NDArray[Shape2D[T2, ONE], GenericDType],
    b: NDArray[Shape2D[T1, ONE], GenericDType],
) -> NDArray[Shape1D[T1], GenericDType]:
    Ax = matmul(A, x)
    Axb = matadd(Ax, b)
    return ravel(Axb)


IN_DIM = Literal[3]
in_dim: IN_DIM = 3

OUT_DIM = Literal[4]
out_dim: OUT_DIM = 4

A: NDArray[Shape2D[OUT_DIM, IN_DIM], np.bool_] = rand_binary_matrix((out_dim, in_dim))
x: NDArray[Shape2D[IN_DIM, ONE], np.bool_] = rand_binary_matrix((in_dim, 1))
b: NDArray[Shape2D[OUT_DIM, ONE], np.bool_] = rand_binary_matrix((out_dim, 1))
y: NDArray[Shape1D[OUT_DIM], np.bool_] = Linear(A, x, b)

# y = Ax + b
print("A:")
print(A.astype(int))
print("x:")
print(x.astype(int))
print("b:")
print(b.astype(int))
print("y:")
print(y.astype(int))
