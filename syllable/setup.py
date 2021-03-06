#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', 'selenium==3.10.0']

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Bernardo Augusto Garcia Loaiza",
    author_email='botibagl@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    description="Package that send a word or words set to service and get the syllabes of each phrase sent",
    entry_points={
        'console_scripts': [
            'syllable=syllable.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='syllable',
    name='syllable',
    packages=find_packages(include=['syllable']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/bgarcial/syllable',
    version='0.1.0',
    zip_safe=False,
)
