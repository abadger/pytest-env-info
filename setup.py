#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-env-info',
    version='0.4.0',
    author='Toshio Kuratomi',
    author_email='a.badger@gmail.com',
    maintainer='Toshio Kuratomi',
    maintainer_email='a.badger@gmail.com',
    license='MIT',
    url='https://github.com/abadger/pytest-env-info',
    description='Push information about the running pytest into envvars',
    long_description=read('README.rst'),
    py_modules=['pytest_env_info'],
    install_requires=['pytest>=3.1.1'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'env-info = pytest_env_info',
        ],
    },
)
