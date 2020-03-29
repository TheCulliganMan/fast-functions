#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import numpy
from setuptools import find_packages, setup, Extension
from Cython.Build import cythonize


extensions = [
    Extension(
        "fast_functions.haversine", 
        ["fast_functions/haversine.pyx"],
        include_dirs=[numpy.get_include()]
    ),
    Extension(
        "fast_functions.geodesic", 
        ["fast_functions/geodesic.pyx"],
        include_dirs=[numpy.get_include()]
    )
]

package_name = "fast_functions"

config = {
    "name": package_name,
    "author": "Ryan Culligan",
    "author_email": "rrculligan@gmail.com",
    "url": "https://github.com/TheCulliganMan/fast-functions",
    "description": "fast-functions",
    "long_description": "fast-functions",
    "license": "MIT",
    "version": "0.0.1",
    "setup_requires": ["Cython"],
    "install_requires": [
        "numpy",
    ],
    "dependency_links": [],
    "classifiers": [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 1 - Planning",
    ],
    "packages": [package_name],
    "ext_modules": cythonize(
        extensions, compiler_directives={"language_level": "3"},
    ),
}

if __name__ == "__main__":
    setup(**config)