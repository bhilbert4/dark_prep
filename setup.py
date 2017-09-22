#! /usr/bin/env python

from setuptools import setup
from setuptools import find_packages

setup(
    name='dark_prep',
    version = '1.0',
    description='Prepare a dark current exposure for use in the NIRCam Data Simulator',
    long_description='A tool to prepare an input dark current exposure for use in the NIRCam Data Simulator. The dark exposure is rearranged into the requested readout pattern, linearized, and cropped to the requested subarray aperture.',
    url='https://github.com/bhilbert4/dark_prep',
    author='Bryan Hilbert',
    author_email='hilbert@stsci.edu',
    keywords = ['astronomy'],
    classifiers = ['Programming Language :: Python'],
    packages = find_packages(exclude=["examples"]),
    install_requires = [],
    include_package_data = True
    )
