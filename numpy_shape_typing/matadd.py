from typing import overload

import numpy as np
from numpy.typing import NDArray

from numpy_shape_typing import T1, T2, GenericType_co, Shape
from numpy_shape_typing.fake_alegebraic import ONE


@overload
def matadd(
    x1: NDArray[Shape[T1], GenericType_co],
    x2: NDArray[Shape[T1], GenericType_co],
    /,
) -> NDArray[Shape[T1], GenericType_co]:
    ...


@overload
def matadd(
    x1: NDArray[Shape[T1, T2], GenericType_co],
    x2: NDArray[Shape[T2], GenericType_co],
    /,
) -> NDArray[Shape[T1, T2], GenericType_co]:
    ...


@overload
def matadd(
    x1: NDArray[Shape[T1, T2], GenericType_co],
    x2: NDArray[Shape[T1, ONE], GenericType_co],
    /,
) -> NDArray[Shape[T1, T2], GenericType_co]:
    ...


@overload
def matadd(
    x1: NDArray[Shape[T1, T2], GenericType_co],
    x2: NDArray[Shape[ONE, T2], GenericType_co],
    /,
) -> NDArray[Shape[T1, T2], GenericType_co]:
    ...


@overload
def matadd(
    x1: NDArray[Shape[T1, T2], GenericType_co],
    x2: NDArray[Shape[T1, T2], GenericType_co],
    /,
) -> NDArray[Shape[T1, T2], GenericType_co]:
    ...


@overload
def matadd(
    x1: GenericType_co,
    x2: NDArray[Shape[T1, T2], GenericType_co],
    /,
) -> NDArray[Shape[T1, T2], GenericType_co]:
    ...


@overload
def matadd(
    x1: NDArray[Shape[T1, T2], GenericType_co],
    x2: GenericType_co,
    /,
) -> NDArray[Shape[T1, T2], GenericType_co]:
    ...


def matadd(x1, x2):
    return np.add(x1, x2)
