# -*- coding: utf-8 -*-
# Copyright (c) 2019 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name='shotgun_api3',
    version='3.8.0',
    description='Flow Production Tracking Python API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Autodesk',
    author_email='https://developer.shotgridsoftware.com',
    url='https://github.com/shotgunsoftware/python-api',
    license="Proprietary",
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    package_data={'': ['cacerts.txt', 'cacert.pem']},
    zip_safe=False,
    python_requires=">=3.7.0",
    install_requires=[
          'httplib2>=0.19.1',
          'certifi>=2022.12.7',
      ],
)
