# -*- encoding: utf-8

import codecs
from setuptools import setup

with codecs.open("README.rst", encoding="utf8") as infile:
    readme_contents = infile.read()

setup(
    name="filecmp2",
    version="1.0.0",
    license="MIT",
    description="Explicit file comparisons",
    long_description=readme_contents,
    author="Alex Chan",
    author_email="alex@alexwlchan.net",
    url="https://github.com/alexwlchan/filecmp2",
    classifiers=[
        "Development Status :: 5 - Production/Stable",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",

        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ]
)
