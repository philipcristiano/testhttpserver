#!/usr/bin/env python

from distribute_setup import use_setuptools
use_setuptools()

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='testhttpserver',
    version='0.1.3',
    description='A HTTP server to use for testing',
    keywords = 'testing',
    url='https://github.com/philipcristiano/testhttpserver',
    author='Philip Cristiano',
    author_email='testhttpserver@philipcristiano.com',
    license='BSD',
    packages=['testhttpserver'],
    install_requires=[''],
    test_suite='tests',
    long_description=read('README.rst'),
    zip_safe=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
    ],
)
