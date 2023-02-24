from typing import Literal

import numpy as np
from numpy.typing import NDArray

from numpy_shape_typing import *
from numpy_shape_typing.fake_alegebraic import ONE
from numpy_shape_typing.matadd import matadd
from numpy_shape_typing.matmul import matmul
from numpy_shape_typing.ravel import ravel


def rand_binary_matrix(shape: ShapeNDType) -> NDArray[ShapeNDType, np.bool_]:
    """Return a random binary matrix."""
    return np.random.randint(low=0, high=2, size=shape, dtype=bool)


def Linear(
    A: NDArray[Shape[T1, T2], GenericType_co],
    x: NDArray[Shape[T2, ONE], GenericType_co],
    b: NDArray[Shape[T1, ONE], GenericType_co],
) -> NDArray[Shape[T1, ONE], GenericType_co]:
    Ax: NDArray[Shape[T1, ONE], GenericType_co] = matmul(A, x)
    return matadd(Ax, b)


FEATURES = Literal[4]
f: FEATURES = 4

A: NDArray[Shape[ONE, FEATURES], np.bool_] = rand_binary_matrix((1, f))
x: NDArray[Shape[FEATURES, ONE], np.bool_] = rand_binary_matrix((f, 1))
b: NDArray[Shape[ONE, ONE], np.bool_] = rand_binary_matrix((1, 1))
y: NDArray[Shape[ONE], np.bool_] = ravel(Linear(A, x, b))

# y = Ax + b
print("A:")
print(A.astype(int))
print("x:")
print(x.astype(int))
print("b:")
print(b.astype(int))
print("y:")
print(y.astype(int))
