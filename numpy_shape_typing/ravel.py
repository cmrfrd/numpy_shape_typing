from typing import overload

from numpy.typing import NDArray

from numpy_shape_typing import T1, GenericType_co, Shape
from numpy_shape_typing.fake_alegebraic import *  # pylint: disable=wildcard-import,unused-wildcard-import


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_TEN, GenericType_co]) -> NDArray[Shape[TEN], GenericType_co]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_NINE, GenericType_co]) -> NDArray[Shape[NINE], GenericType_co]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_EIGHT, GenericType_co]) -> NDArray[Shape[EIGHT], GenericType_co]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_SEVEN, GenericType_co]) -> NDArray[Shape[SEVEN], GenericType_co]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_SIX, GenericType_co]) -> NDArray[Shape[SIX], GenericType_co]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_FIVE, GenericType_co]) -> NDArray[Shape[FIVE], GenericType_co]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_FOUR, GenericType_co]) -> NDArray[Shape[FOUR], GenericType_co]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_THREE, GenericType_co]) -> NDArray[Shape[THREE], GenericType_co]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_TWO, GenericType_co]) -> NDArray[Shape[TWO], GenericType_co]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_ONE, GenericType_co]) -> NDArray[Shape[ONE], GenericType_co]:
    ...


@overload
def ravel(arr: NDArray[Shape[T1], GenericType_co]) -> NDArray[Shape[T1], GenericType_co]:
    ...


def ravel(arr):
    return arr.ravel()
