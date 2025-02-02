#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import annotations

from distutils.core import setup

with open("README.md") as f:
    LONG_DESCRIPTION, LONG_DESC_TYPE = f.read(), "text/markdown"


setup(
    name="TMP1075",
    version="0.2.2",
    description="A python wrapper for interacting with the TMP1075",
    author="Cam Davidson-Pilon",
    author_email="cam@pioreactor.com",
    url="https://github.com/Pioreactor/TMP1075",
    packages=["TMP1075"],
    package_data={"TMP1075": ["py.typed"]},
    license="MIT",
    python_requires=">=3.6",
    install_requires=["Adafruit-Blinka", "adafruit-circuitpython-busdevice"],
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
)
