import typing
from functools import reduce
from itertools import product
from operator import mul
from typing import Literal, Tuple, Union

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

SHAPE_2D_MUL_TO_TEN = Union[
    typing.Tuple[typing.Literal[1], typing.Literal[10]],
    typing.Tuple[typing.Literal[2], typing.Literal[5]],
    typing.Tuple[typing.Literal[5], typing.Literal[2]],
    typing.Tuple[typing.Literal[10], typing.Literal[1]],
]
SHAPE_2D_MUL_TO_NINE = Union[
    typing.Tuple[typing.Literal[1], typing.Literal[9]],
    typing.Tuple[typing.Literal[3], typing.Literal[3]],
    typing.Tuple[typing.Literal[9], typing.Literal[1]],
]
SHAPE_2D_MUL_TO_EIGHT = Union[
    typing.Tuple[typing.Literal[1], typing.Literal[8]],
    typing.Tuple[typing.Literal[2], typing.Literal[4]],
    typing.Tuple[typing.Literal[4], typing.Literal[2]],
    typing.Tuple[typing.Literal[8], typing.Literal[1]],
]
SHAPE_2D_MUL_TO_SEVEN = Union[
    typing.Tuple[typing.Literal[1], typing.Literal[7]], typing.Tuple[typing.Literal[7], typing.Literal[1]]
]
SHAPE_2D_MUL_TO_SIX = Union[
    typing.Tuple[typing.Literal[1], typing.Literal[6]],
    typing.Tuple[typing.Literal[2], typing.Literal[3]],
    typing.Tuple[typing.Literal[3], typing.Literal[2]],
    typing.Tuple[typing.Literal[6], typing.Literal[1]],
]
SHAPE_2D_MUL_TO_FIVE = Union[
    typing.Tuple[typing.Literal[1], typing.Literal[5]], typing.Tuple[typing.Literal[5], typing.Literal[1]]
]
SHAPE_2D_MUL_TO_FOUR = Union[
    typing.Tuple[typing.Literal[1], typing.Literal[4]],
    typing.Tuple[typing.Literal[2], typing.Literal[2]],
    typing.Tuple[typing.Literal[4], typing.Literal[1]],
]
SHAPE_2D_MUL_TO_THREE = Union[
    typing.Tuple[typing.Literal[1], typing.Literal[3]], typing.Tuple[typing.Literal[3], typing.Literal[1]]
]
SHAPE_2D_MUL_TO_TWO = Union[
    typing.Tuple[typing.Literal[1], typing.Literal[2]], typing.Tuple[typing.Literal[2], typing.Literal[1]]
]
SHAPE_2D_MUL_TO_ONE = typing.Tuple[typing.Literal[1], typing.Literal[1]]


## Code gen tools
def literal_to_int(inp):
    return inp.__args__[0]


def get_nd_shapes_for_ravel(factors: list, final_dim_size: int, start_dim: int):
    return list(
        filter(
            lambda seq: reduce(mul, map(literal_to_int, seq), 1) == final_dim_size,
            product(filter(lambda i: literal_to_int(i) <= final_dim_size, factors), repeat=start_dim),
        )
    )


def get_shapes(inp_shapes) -> list:
    return list(Tuple[*inp_shape] for inp_shape in inp_shapes)
