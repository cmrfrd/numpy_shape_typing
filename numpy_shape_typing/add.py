from typing import overload

import numpy as np
from numpy.typing import NDArray

from numpy_shape_typing.types import ONE, T1, T2, GenericDType, Shape1D, Shape2D, ShapeVarGen


@overload
def add(
    x1: NDArray[Shape2D[T1, T2], GenericDType],
    x2: NDArray[Shape1D[T2], GenericDType],
    /,
) -> NDArray[Shape2D[T1, T2], GenericDType]:
    ...


@overload
def add(
    x1: NDArray[Shape1D[T2], GenericDType],
    x2: NDArray[Shape2D[T1, T2], GenericDType],
    /,
) -> NDArray[Shape2D[T1, T2], GenericDType]:
    ...


@overload
def add(
    x1: NDArray[Shape2D[T1, T2], GenericDType],
    x2: NDArray[Shape1D[ONE], GenericDType],
    /,
) -> NDArray[Shape2D[T1, T2], GenericDType]:
    ...


@overload
def add(
    x1: NDArray[Shape1D[ONE], GenericDType],
    x2: NDArray[Shape2D[T1, T2], GenericDType],
    /,
) -> NDArray[Shape2D[T1, T2], GenericDType]:
    ...


@overload
def add(
    x1: NDArray[Shape2D[T1, T2], GenericDType],
    x2: NDArray[Shape2D[T1, ONE], GenericDType],
    /,
) -> NDArray[Shape2D[T1, T2], GenericDType]:
    ...


@overload
def add(
    x1: NDArray[Shape2D[T1, T2], GenericDType],
    x2: NDArray[Shape2D[ONE, T2], GenericDType],
    /,
) -> NDArray[Shape2D[T1, T2], GenericDType]:
    ...


@overload
def add(
    x1: NDArray[Shape2D[T1, ONE], GenericDType],
    x2: NDArray[Shape2D[T1, T2], GenericDType],
    /,
) -> NDArray[Shape2D[T1, T2], GenericDType]:
    ...


@overload
def add(
    x1: NDArray[Shape2D[ONE, T2], GenericDType],
    x2: NDArray[Shape2D[T1, T2], GenericDType],
    /,
) -> NDArray[Shape2D[T1, T2], GenericDType]:
    ...


@overload
def add(
    x1: GenericDType,
    x2: NDArray[Shape2D[T1, T2], GenericDType],
    /,
) -> NDArray[Shape2D[T1, T2], GenericDType]:
    ...


@overload
def add(
    x1: NDArray[Shape2D[T1, T2], GenericDType],
    x2: GenericDType,
    /,
) -> NDArray[Shape2D[T1, T2], GenericDType]:
    ...


@overload
def add(
    x1: NDArray[*ShapeVarGen, GenericDType],
    x2: NDArray[*ShapeVarGen, GenericDType],
    /,
) -> NDArray[*ShapeVarGen, GenericDType]:
    ...


def add(x1, x2):
    return np.add(x1, x2)
