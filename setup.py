#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import djangogeo
version = djangogeo.__version__

setup(
    name='Django Geo',
    version=version,
    author="Savio Abuga",
    author_email='Savio Abuga',
    packages=[
        'djangogeo',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.4',
    ],
    zip_safe=False,
    scripts=['djangogeo/manage.py'],
)
