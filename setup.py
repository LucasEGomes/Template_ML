from os import path
from setuptools import find_packages, setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description=path.basename(this_directory),
    author='Lucas Eduardo Gomes',
    long_description=long_description,
    long_description_content_type='text/markdown',
)