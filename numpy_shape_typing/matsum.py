from typing import Any, Literal, Optional, overload

import numpy as np
from numpy.typing import NDArray

from numpy_shape_typing import T1, T2, GenericType_co, Shape


@overload
def matsum(
    x1: NDArray[Shape[T1, T2], GenericType_co], axis: Literal[1], /
) -> NDArray[Shape[T1], GenericType_co]:
    ...


@overload
def matsum(
    x1: NDArray[Shape[T1, T2], GenericType_co], axis: Literal[0], /
) -> NDArray[Shape[T2], GenericType_co]:
    ...


@overload
def matsum(x1: NDArray[Shape[T1, T2], GenericType_co], axis: None = None, /) -> GenericType_co:
    ...


@overload
def matsum(x1: NDArray[Shape[T1], GenericType_co], axis: Literal[0], /) -> GenericType_co:
    ...


@overload
def matsum(x1: NDArray[Shape[T1], GenericType_co], axis: None = None, /) -> GenericType_co:
    ...


def matsum(x1, axis: Optional[Any] = None):
    return np.sum(x1, axis=axis)
