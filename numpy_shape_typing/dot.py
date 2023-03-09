from typing import overload

import numpy as np
from numpy.typing import NDArray

from numpy_shape_typing.types import T1, T2, T3, GenericDType, Shape, Shape1D, Shape2D, ShapeVarGen


@overload
def dot(x1: NDArray[Shape1D[T1], GenericDType], x2: NDArray[Shape1D[T1], GenericDType], /) -> GenericDType:
    ...


@overload
def dot(
    x1: NDArray[Shape[T1, *ShapeVarGen], GenericDType], x2: NDArray[Shape1D[T1], GenericDType], /
) -> NDArray[Shape[*ShapeVarGen], GenericDType]:
    ...


@overload
def dot(
    x1: NDArray[Shape2D[T1, T2], GenericDType],
    x2: NDArray[Shape2D[T2, T3], GenericDType],
    /,
) -> NDArray[Shape2D[T1, T3], GenericDType]:
    ...


@overload
def dot(x1: GenericDType, x2: GenericDType, /) -> GenericDType:
    ...


def dot(x1, x2):
    return np.dot(x1, x2)
