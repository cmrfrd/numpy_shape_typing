from typing import overload

from numpy.typing import NDArray

from numpy_shape_typing.fake_alegebraic import (
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
    Shape1D,
    Shape2D,
)


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_TEN, GenericDType]) -> NDArray[Shape1D[TEN], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_NINE, GenericDType]) -> NDArray[Shape1D[NINE], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_EIGHT, GenericDType]) -> NDArray[Shape1D[EIGHT], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_SEVEN, GenericDType]) -> NDArray[Shape1D[SEVEN], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_SIX, GenericDType]) -> NDArray[Shape1D[SIX], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_FIVE, GenericDType]) -> NDArray[Shape1D[FIVE], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_FOUR, GenericDType]) -> NDArray[Shape1D[FOUR], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_THREE, GenericDType]) -> NDArray[Shape1D[THREE], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_TWO, GenericDType]) -> NDArray[Shape1D[TWO], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_ONE, GenericDType]) -> NDArray[Shape1D[ONE], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[Shape2D[T1, ONE], GenericDType]) -> NDArray[Shape1D[T1], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[Shape2D[ONE, T1], GenericDType]) -> NDArray[Shape1D[T1], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[Shape1D[T1], GenericDType]) -> NDArray[Shape1D[T1], GenericDType]:
    ...


def ravel(arr):
    return arr.ravel()
