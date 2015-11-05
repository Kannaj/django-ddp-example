#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='django-ddp-example',
    version='0.0.1',
    description='Django DDP example Todo project.',
    long_description=open('README.rst').read(),
    author='Kannaj',
    author_email='kannaj@example.com',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Django>=1.8.5',
        'django-ddp>=0.18.0',
    ],
)
