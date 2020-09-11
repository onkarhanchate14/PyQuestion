import pathlib
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

VERSION = '0.1.0'
AUTHOR = 'Onkar Hanchate'
AUTHOR_EMAIL = 'onkarhanchate14@gmail.com'
URL = 'https://github.com/onkarhanchate14/PyQuestion'

LICENSE = 'Apache License 2.0'
DESCRIPTION = 'Return a variety of Python problem/question to solve'
LONG_DESCRIPTION = long_description
LONG_DESC_TYPE = "text/markdown"


setup(name='PyQuestion',
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      packages=find_packages()
      )
