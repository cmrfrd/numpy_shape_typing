# Numpy shape typing

alex@taoa.io

This repo is a POC of using [Variadic Generics](https://peps.python.org/pep-0646/) in [pyright](https://github.com/microsoft/pyright) to shape type numpy arrays.

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

2. Open `src/__init__.py` and try modifying the types of the linear equation implementation at the bottom on the file
