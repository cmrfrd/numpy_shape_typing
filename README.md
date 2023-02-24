# Numpy shape typing

alex@taoa.io

This repo is a POC of using [Variadic Generics](https://peps.python.org/pep-0646/) and [pyright](https://github.com/microsoft/pyright) to shape type numpy arrays.

This gives us the ability to include shape types so we can write numpy code like this:

```
def Linear(
    A: NDArray[Shape[T1, T2], GenericType_co],
    x: NDArray[Shape[T2, ONE], GenericType_co],
    b: NDArray[Shape[T1, ONE], GenericType_co],
) -> NDArray[Shape[T1, ONE], GenericType_co]:
    Ax: NDArray[Shape[T1, ONE], GenericType_co] = matmul(A, x)
    return matadd(Ax, b)
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

2. Open `src/__init__.py` in a VSCode / codespaces and try modifying the types of the linear equation implementation at the bottom on the file.
