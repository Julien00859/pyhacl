import itertools
import os
import pathlib
from setuptools import Extension, setup
from Cython.Build import cythonize

root = pathlib.Path(__file__).parent
hacl_packages = root.joinpath('hacl-packages')
include_dirs = [
    os.fspath(include_dir)
    for include_dir, _
    in itertools.groupby(
        hacl_packages.glob('**/*.h'),
        lambda path: path.parent
    )
    if 'benchmarks' not in include_dir.parents
    if 'build' not in include_dir.parents
    if 'config' not in include_dir.parents
    if 'msvc' not in include_dir.parents
    if 'rust' not in include_dir.parents
    if 'tests' not in include_dir.parents
]

setup(
    ext_modules=cythonize([
        Extension(
            name="pyhacl.hashlib",
            sources=["src/pyhacl/_hashlib.py"],
            include_dirs=include_dirs,
        ),
    ], annotate=True)
)
