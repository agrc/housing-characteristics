#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
setup.py
A module that installs housing-unit-inventory as a module
"""
from glob import glob
from os.path import basename, splitext

from setuptools import find_packages, setup

setup(
    name='ugrc-housing-unit-inventory',
    version='1.0.0',
    license='',
    description='Analyze the housing inventory of a county or other geography',
    author='Josh Reynolds, WFRC; Jake Adams, UGRC',
    author_email='jdadams@utah.gov',
    url='https://github.com/agrc/housing-unit-inventory',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=True,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
    ],
    project_urls={
        'Issue Tracker': 'https://github.com/agrc/housing-unit-inventory/issues',
    },
    keywords=['gis'],
    install_requires=[
        'pandas==1.3.*',
        'numpy==1.20.*',
        'arcgis==1.9.*',
    ],
    extras_require={
        'tests': [
            'pylint-quotes==0.2.*',
            'pylint==2.5.*',
            'pytest-cov==2.9.*',
            'pytest-instafail==0.4.*',
            'pytest-isort==1.0.*',
            'pytest-pylint==0.14.*',
            'pytest-watch==4.2.*',
            'pytest==4.*',
            'yapf==0.30.*',
            'pytest-mock==3.2.*',
        ]
    },
    setup_requires=[
        'pytest-runner',
    ],
    entry_points={'console_scripts': [
        'housing-unit-inventory = housing_unit-inventory.main:process',
    ]},
)
