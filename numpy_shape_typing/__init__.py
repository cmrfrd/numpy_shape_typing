"""
Example of using numpy.typing with numpy 1.20.0 to type-check a function
with shape and dtype annotations.
"""

from typing import Literal, Tuple, TypeVar, TypeVarTuple, Unpack

import numpy as np

from numpy_shape_typing.fake_alegebraic import ALL_NUMS_Union

T1 = TypeVar("T1", bound=ALL_NUMS_Union)
T2 = TypeVar("T2", bound=ALL_NUMS_Union)
T3 = TypeVar("T3", bound=ALL_NUMS_Union)
T4 = TypeVar("T4", bound=ALL_NUMS_Union)
T5 = TypeVar("T5", bound=ALL_NUMS_Union)
Shape = Tuple
Shape1D = Shape[T1]
Shape2D = Shape[T1, T2]
ShapeND = Shape[T1, ...]
Shape1DType = TypeVar("Shape1DType", bound=Shape1D)
Shape2DType = TypeVar("Shape2DType", bound=Shape2D)
ShapeNDType = TypeVar("ShapeNDType", bound=ShapeND)
ShapeVarGen = TypeVarTuple("ShapeVarGen")
GenericType_co = TypeVar("GenericType_co", bound=np.generic)
