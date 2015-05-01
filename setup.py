#!/usr/bin/env python

import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()

REQUIREMENTS = [
    'boto',
    'requests >= 2.6.0',
    'mock >= 1.0.1',
    'nose >= 1.3.4',
    'tox >= 1.9.0',
    'flake8==2.4.0'
]

KEYWORDS = [
    'deployment',
    'verification',
]

setup(
    name='ec2-handler',
    version='0.1.3',
    description='ec2-handler',
    long_description=README,
    author='Richard Pappalardo',
    author_email='rpappalax@gmail.com',
    url='https://github.com/rpappalax/ec2-handler',
    license="MIT",
    install_requires=REQUIREMENTS,
    keywords=KEYWORDS,
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
    ],
    entry_points={
        'console_scripts': ['verify = verify.demo_handler:main']
    },
)
