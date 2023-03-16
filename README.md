# Numpy shape typing

alex@taoa.io

This repo is a POC of using [Variadic Generics](https://peps.python.org/pep-0646/) and [pyright](https://github.com/microsoft/pyright) to shape type numpy arrays.

This gives us the ability to include shape types so we can write numpy code like this:

```python
def Linear(
    A: NDArray[Shape2D[T1, T2], GenericDType],
    x: NDArray[Shape2D[T2, ONE], GenericDType],
    b: NDArray[Shape2D[T1, ONE], GenericDType],
) -> NDArray[Shape1D[T1], GenericDType]:
    Ax = dot(A, x)
    Axb = add(Ax, b)
    return ravel(Axb)
```

For accessibility and reproducibility, a devcontainer + docker is provided.

## How to run

1. Clone the repo and checkout custom numpy

```
git clone https://github.com/cmrfrd/numpy_shape_typing
git submodule update --init --recursive --remote
pushd submodules/numpy
git checkout v1.24.2.dev1
popd
```

2. Open `src/linear.py` in a VSCode / codespaces and try modifying the types of the linear implementation.
