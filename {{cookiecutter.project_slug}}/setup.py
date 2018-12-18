#!/usr/bin/env python

import pathlib

from setuptools import find_packages, setup

version = __import__('{{cookiecutter.project_package}}').__version__

requirements = [
    'aioworkers>=0.12.0',
]

test_requirements = [
    'pytest',
    'pytest-runner',
    'pytest-aiohttp',
    'pytest-flake8',
    'flake8-isort',
]

readme = pathlib.Path('README.rst').read_text()


setup(
    name='{{cookiecutter.project_slug}}',
    version=version,
    description='{{cookiecutter.description}}',
    long_description=readme,
    author='{{cookiecutter.author_name}}',
    author_email='{{cookiecutter.email}}',
    url='https://github.com/aioworkers/{{cookiecutter.project_slug}}',
    packages=[
        i for i in find_packages()
        if i.startswith('{{cookiecutter.project_package}}')
    ],
    include_package_data=True,
    install_requires=requirements,
    license='Apache Software License 2.0',
    keywords='aioworkers',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
