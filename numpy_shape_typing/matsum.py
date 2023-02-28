from typing import Any, Literal, Optional, overload

import numpy as np
from numpy.typing import NDArray

from numpy_shape_typing import T1, T2, GenericDType, Shape


@overload
def matsum(x1: NDArray[Shape[T1, T2], GenericDType], axis: Literal[1], /) -> NDArray[Shape[T1], GenericDType]:
    ...


@overload
def matsum(x1: NDArray[Shape[T1, T2], GenericDType], axis: Literal[0], /) -> NDArray[Shape[T2], GenericDType]:
    ...


@overload
def matsum(x1: NDArray[Shape[T1, T2], GenericDType], axis: None = None, /) -> GenericDType:
    ...


@overload
def matsum(x1: NDArray[Shape[T1], GenericDType], axis: Literal[0], /) -> GenericDType:
    ...


@overload
def matsum(x1: NDArray[Shape[T1], GenericDType], axis: None = None, /) -> GenericDType:
    ...


def matsum(x1, axis: Optional[Any] = None):
    return np.sum(x1, axis=axis)
