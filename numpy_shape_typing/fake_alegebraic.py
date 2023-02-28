import typing
from functools import reduce
from itertools import product
from operator import mul
from typing import Literal, Tuple, TypeVar, TypeVarTuple, Union, Unpack

import numpy as np

ONE = Literal[1]
TWO = Literal[2]
THREE = Literal[3]
FOUR = Literal[4]
FIVE = Literal[5]
SIX = Literal[6]
SEVEN = Literal[7]
EIGHT = Literal[8]
NINE = Literal[9]
TEN = Literal[10]
ALL_NUMS = tuple([ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN])
ALL_NUMS_Union = Union[ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN]

T1 = TypeVar("T1", bound=ALL_NUMS_Union)
T2 = TypeVar("T2", bound=ALL_NUMS_Union)
T3 = TypeVar("T3", bound=ALL_NUMS_Union)
T4 = TypeVar("T4", bound=ALL_NUMS_Union)
T5 = TypeVar("T5", bound=ALL_NUMS_Union)
Shape = Tuple
Shape1D = Shape[T1]
Shape2D = Shape[T1, T2]
Shape1DType = TypeVar("Shape1DType", bound=Shape1D)
Shape2DType = TypeVar("Shape2DType", bound=Shape2D)
ShapeVarGen = TypeVarTuple("ShapeVarGen")
ShapeND = Shape[ALL_NUMS_Union, ...]
ShapeNDType = TypeVar("ShapeNDType", bound=ShapeND)
GenericDType = TypeVar("GenericDType", bound=np.generic)

SHAPE_2D_MUL_TO_TEN = Union[
    Shape2D[typing.Literal[1], typing.Literal[10]],
    Shape2D[typing.Literal[2], typing.Literal[5]],
    Shape2D[typing.Literal[5], typing.Literal[2]],
    Shape2D[typing.Literal[10], typing.Literal[1]],
]
SHAPE_2D_MUL_TO_NINE = Union[
    Shape2D[typing.Literal[1], typing.Literal[9]],
    Shape2D[typing.Literal[3], typing.Literal[3]],
    Shape2D[typing.Literal[9], typing.Literal[1]],
]
SHAPE_2D_MUL_TO_EIGHT = Union[
    Shape2D[typing.Literal[1], typing.Literal[8]],
    Shape2D[typing.Literal[2], typing.Literal[4]],
    Shape2D[typing.Literal[4], typing.Literal[2]],
    Shape2D[typing.Literal[8], typing.Literal[1]],
]
SHAPE_2D_MUL_TO_SEVEN = Union[
    Shape2D[typing.Literal[1], typing.Literal[7]], Shape2D[typing.Literal[7], typing.Literal[1]]
]
SHAPE_2D_MUL_TO_SIX = Union[
    Shape2D[typing.Literal[1], typing.Literal[6]],
    Shape2D[typing.Literal[2], typing.Literal[3]],
    Shape2D[typing.Literal[3], typing.Literal[2]],
    Shape2D[typing.Literal[6], typing.Literal[1]],
]
SHAPE_2D_MUL_TO_FIVE = Union[
    Shape2D[typing.Literal[1], typing.Literal[5]], Shape2D[typing.Literal[5], typing.Literal[1]]
]
SHAPE_2D_MUL_TO_FOUR = Union[
    Shape2D[typing.Literal[1], typing.Literal[4]],
    Shape2D[typing.Literal[2], typing.Literal[2]],
    Shape2D[typing.Literal[4], typing.Literal[1]],
]
SHAPE_2D_MUL_TO_THREE = Union[
    Shape2D[typing.Literal[1], typing.Literal[3]], Shape2D[typing.Literal[3], typing.Literal[1]]
]
SHAPE_2D_MUL_TO_TWO = Union[
    Shape2D[typing.Literal[1], typing.Literal[2]], Shape2D[typing.Literal[2], typing.Literal[1]]
]
SHAPE_2D_MUL_TO_ONE = Shape2D[typing.Literal[1], typing.Literal[1]]


## Code gen tools
def get_nd_shapes_for_ravel(factors: list, final_dim_size: int, start_dim: int):
    return list(
        filter(
            lambda seq: reduce(mul, map(lambda i: i.__args__[0], seq), 1) == final_dim_size,
            product(filter(lambda i: i.__args__[0] <= final_dim_size, factors), repeat=start_dim),
        )
    )


def get_shapes(inp_shapes) -> list:
    return list(Tuple[*inp_shape] for inp_shape in inp_shapes)
