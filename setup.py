#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import numpy
from setuptools import find_packages, setup
from Cython.Build import cythonize


def find_pyx(package_name):
    path = f"./{package_name}"
    pyx_files = []
    for root, _, filenames in os.walk(path):
        for fname in filenames:
            if fname.endswith(".pyx"):
                pyx_files.append(os.path.join(root, fname))
    return pyx_files


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
        find_pyx(package_name), compiler_directives={"language_level": "3"},
    ),
    "include_dirs": [numpy.get_include()]
}

if __name__ == "__main__":
    setup(**config)