from typing import TypeVar

import numpy as np
from numpy.typing import NDArray

GenericDType = TypeVar("GenericDType", bound=np.generic)


def Linear(
    A: NDArray[GenericDType],
    x: NDArray[GenericDType],
    b: NDArray[GenericDType],
) -> NDArray[GenericDType]:
    """
    Args:
        A: ndarray of shape (M x N)
        x: ndarray of shape (N x 1)
        b: ndarray of shape (M x 1)

    Returns:
        Linear output ndarray of shape (M)
    """
    assert len(A.shape) == 2, f"A must be of dim 2, not {len(A.shape)}"
    Am, An = A.shape

    assert x.shape == (An, 1), f"X must be shape ({An}, 1) to do matmul"
    Ax: NDArray[GenericDType] = np.matmul(A, x)  # Shape (M x 1)

    assert b.shape == (Am, 1), f"Bias term must be shape ({Am}, 1)"
    result: NDArray[GenericDType] = np.add(Ax, b)  # (M x 1) + (M x 1)

    ravel_result: NDArray[GenericDType] = np.ravel(result)
    assert ravel_result.shape == (Am,), f"Uh oh, ravel result is shape {ravel_result.shape} and not {(Am,)}"
    return ravel_result


A: NDArray[np.uint8] = np.random.randint(low=0, high=2, size=(10, 10), dtype=np.uint8)
x: NDArray[np.uint8] = np.random.randint(low=0, high=2, size=(10, 10), dtype=np.uint8)
b: NDArray[np.uint16] = np.random.randint(low=0, high=2, size=(10, 10), dtype=np.uint16)
y: NDArray[np.uint8] = Linear(A, x, b)
