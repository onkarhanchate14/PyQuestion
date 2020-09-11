import pathlib
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

VERSION = '0.1.0'
PACKAGE_NAME = 'PyQuestion'
AUTHOR = 'Onkar Hanchate'
AUTHOR_EMAIL = 'onkarhanchate14@gmail.com'
URL = 'https://github.com/onkarhanchate14/PyQuestion'

LICENSE = 'Apache License 2.0'
DESCRIPTION = 'Return a variety of Python problem/question to solve'
LONG_DESCRIPTION = long_description
LONG_DESC_TYPE = "text/markdown"


setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      packages=setuptools.find_packages()
      )
