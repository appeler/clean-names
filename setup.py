#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name="clean-names",
      version="0.2.0",
      description="Clean a list of names",
      license="MIT",
      install_requires=["nameparser"],
      author_email="gsood07@gmail.com",
      url="http://github.com/soodoku/clean-names",
      packages=find_packages(),
      keywords="human names",
      classifiers=['Development Status :: 4 - Beta'],
      zip_safe=True)