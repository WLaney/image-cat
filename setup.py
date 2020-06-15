#!/usr/bin/env python3

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
with open("requirements.txt", "r") as fh:
    requirements = fh.read()

setuptools.setup(
    name="image_cat",
    version="0.0.1",
    author="William Laney",
    author_email="williamlaney@yahoo.com",
    description="Concatenate Two Images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires = requirements,
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    scripts=['image_cat/image_cat'],
)
