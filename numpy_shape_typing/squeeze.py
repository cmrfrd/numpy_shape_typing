from typing import Literal, overload

import numpy as np
from numpy.typing import NDArray

from numpy_shape_typing.types import (
    EIGHT,
    FIVE,
    FOUR,
    NINE,
    ONE,
    SEVEN,
    SHAPE_2D_MUL_TO_EIGHT,
    SHAPE_2D_MUL_TO_FIVE,
    SHAPE_2D_MUL_TO_FOUR,
    SHAPE_2D_MUL_TO_NINE,
    SHAPE_2D_MUL_TO_ONE,
    SHAPE_2D_MUL_TO_SEVEN,
    SHAPE_2D_MUL_TO_SIX,
    SHAPE_2D_MUL_TO_TEN,
    SHAPE_2D_MUL_TO_THREE,
    SHAPE_2D_MUL_TO_TWO,
    SIX,
    T1,
    TEN,
    THREE,
    TWO,
    GenericDType,
    Shape,
    Shape1D,
    ShapeND,
    ShapeVarGen,
)


@overload
def squeeze(
    arr: NDArray[Shape[T1, ONE, *ShapeVarGen], GenericDType], axis: Literal[1]
) -> NDArray[Shape[T1, *ShapeVarGen], GenericDType]:
    ...


@overload
def squeeze(arr: NDArray[Shape[T1, ONE], GenericDType], axis: Literal[1]) -> NDArray[Shape[T1], GenericDType]:
    ...


@overload
def squeeze(
    arr: NDArray[Shape[*ShapeVarGen, ONE], GenericDType], axis: Literal[-1]
) -> NDArray[Shape[*ShapeVarGen], GenericDType]:
    ...


@overload
def squeeze(
    arr: NDArray[Shape[ONE, *ShapeVarGen], GenericDType], axis: Literal[0]
) -> NDArray[Shape[*ShapeVarGen], GenericDType]:
    ...


def squeeze(arr, axis):
    return np.squeeze(arr, axis)
