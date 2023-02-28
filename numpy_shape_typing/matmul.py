from typing import overload

import numpy as np
from numpy.typing import NDArray

from numpy_shape_typing.fake_alegebraic import T1, T2, T3, GenericDType, Shape


@overload
def matmul(x1: NDArray[Shape[T1], GenericDType], x2: NDArray[Shape[T1], GenericDType], /) -> GenericDType:
    ...


@overload
def matmul(
    x1: NDArray[Shape[T1], GenericDType], x2: NDArray[Shape[T1, T2], GenericDType], /
) -> NDArray[Shape[T2], GenericDType]:
    ...


@overload
def matmul(
    x1: NDArray[Shape[T1, T2], GenericDType], x2: NDArray[Shape[T2], GenericDType], /
) -> NDArray[Shape[T1], GenericDType]:
    ...


@overload
def matmul(
    x1: NDArray[Shape[T1, T2], GenericDType],
    x2: NDArray[Shape[T2, T3], GenericDType],
    /,
) -> NDArray[Shape[T1, T3], GenericDType]:
    ...


def matmul(x1, x2):
    return np.matmul(x1, x2)
