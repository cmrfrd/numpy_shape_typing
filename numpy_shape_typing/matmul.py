from typing import overload

import numpy as np
from numpy.typing import NDArray

from numpy_shape_typing import T1, T2, T3, GenericType_co, Shape


@overload
def matmul(
    x1: NDArray[Shape[T1], GenericType_co], x2: NDArray[Shape[T1], GenericType_co], /
) -> GenericType_co:
    ...


@overload
def matmul(
    x1: NDArray[Shape[T1], GenericType_co], x2: NDArray[Shape[T1, T2], GenericType_co], /
) -> NDArray[Shape[T2], GenericType_co]:
    ...


@overload
def matmul(
    x1: NDArray[Shape[T1, T2], GenericType_co], x2: NDArray[Shape[T2], GenericType_co], /
) -> NDArray[Shape[T1], GenericType_co]:
    ...


@overload
def matmul(
    x1: NDArray[Shape[T1, T2], GenericType_co],
    x2: NDArray[Shape[T2, T3], GenericType_co],
    /,
) -> NDArray[Shape[T1, T3], GenericType_co]:
    ...


def matmul(x1, x2):
    return np.matmul(x1, x2)
