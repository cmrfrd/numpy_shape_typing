"""
Example of using numpy.typing with numpy 1.20.0 to type-check a function
with shape and dtype annotations.
"""

from typing import Literal, Tuple, TypeVar, overload

import numpy as np
from numpy.typing import NDArray

ONE = Literal[1]
T1 = TypeVar("T1", bound=int)
T2 = TypeVar("T2", bound=int)
T3 = TypeVar("T3", bound=int)
T4 = TypeVar("T4", bound=int)
T5 = TypeVar("T5", bound=int)
Shape = Tuple
ShapeType = TypeVar("ShapeType", bound=Tuple[int, ...])
GenericType_co = TypeVar("GenericType_co", bound=np.generic, covariant=True)


##
## 2D matmul with shape and dtype annotations
##


@overload
def matmul(
    x1: NDArray[Shape[T1], GenericType_co], x2: NDArray[Shape[T1], GenericType_co], /
) -> GenericType_co:
    ...


@overload
def matmul(
    x1: NDArray[Shape[T1], GenericType_co], x2: NDArray[Shape[T1, T2], GenericType_co], /
) -> NDArray[Shape[T2], GenericType_co]:
    ...


@overload
def matmul(
    x1: NDArray[Shape[T1, T2], GenericType_co], x2: NDArray[Shape[T2], GenericType_co], /
) -> NDArray[Shape[T1], GenericType_co]:
    ...


@overload
def matmul(
    x1: NDArray[Shape[T1, T2], GenericType_co],
    x2: NDArray[Shape[T2, T3], GenericType_co],
    /,
) -> NDArray[Shape[T1, T3], GenericType_co]:
    ...


def matmul(x1, x2):
    return np.matmul(x1, x2)


##
## 2D matsum with shape and dtype annotations
##


@overload
def matsum(
    x1: NDArray[Shape[T1, T2], GenericType_co], axis: Literal[1], /
) -> NDArray[Shape[T1], GenericType_co]:
    ...


@overload
def matsum(
    x1: NDArray[Shape[T1, T2], GenericType_co], axis: Literal[0], /
) -> NDArray[Shape[T2], GenericType_co]:
    ...


@overload
def matsum(x1: NDArray[Shape[T1], GenericType_co], axis: Literal[0], /) -> GenericType_co:
    ...


def matsum(x1, axis=0):
    return np.sum(x1, axis=axis)


##
## 2D matadd with shape and dtype annotations
##


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


def matadd(x1, x2):
    return np.add(x1, x2)


def rand_binary_matrix(shape: ShapeType) -> NDArray[ShapeType, np.bool_]:
    return np.random.randint(low=0, high=2, size=shape, dtype=bool)


FEATURES = Literal[4]
f: FEATURES = 4

A: NDArray[Shape[ONE, FEATURES], np.bool_] = rand_binary_matrix((1, f))
x: NDArray[Shape[FEATURES, ONE], np.bool_] = rand_binary_matrix((f, 1))
Ax: NDArray[Shape[ONE, ONE], np.bool_] = matmul(A, x)
b: NDArray[Shape[ONE], np.bool_] = rand_binary_matrix((1,))
y: NDArray[Shape[ONE, ONE], np.bool_] = matadd(Ax, b)

# y = Ax + b
print("A:")
print(A.astype(int))
print("x:")
print(x.astype(int))
print("Ax:")
print(Ax.astype(int))
print("b:")
print(b.astype(int))
print("y:")
print(y.astype(int))
