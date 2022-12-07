# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import os

from setuptools import find_packages
from setuptools import setup

here = os.path.dirname(__file__)


def read_requirements(file_):
    with open(os.path.join(here, file_)) as f:
        return sorted(list(set(line.split("#")[0].strip() for line in f)))


install_requires = read_requirements("requirements.txt")


with open(os.path.join(here, 'VERSION')) as f:
    version = f.read().strip()

setup(
    name='reachablelib',
    version=version,
    description='Library to find unreachable code',
    author='Marco Castelluccio',
    author_email='mcastelluccio@mozilla.com',
    install_requires=install_requires,
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    include_package_data=True,
    license='MPL2',
)
