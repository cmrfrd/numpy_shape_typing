import numpy as np
from numpy.typing import NDArray

from numpy_shape_typing.types import ShapeNDType


def rand_normal_matrix(shape: ShapeNDType) -> NDArray[ShapeNDType, np.float64]:
    """Return a random ND normal matrix."""
    return np.random.standard_normal(size=shape)
