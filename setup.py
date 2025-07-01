from distutils.core import setup
from setuptools import find_packages

setup(name='pkg_setup',
      version='1.0.0',
      description='Testing out publishing the pyuthon packages with simple print functions and python methods',
      author='ghujgt',
      author_email='ghujgt@gmail.com',
    #   url='https://www.python.org/sigs/distutils-sig/',
      packages=find_packages(),
      license = "MIT",
      classifiers = ["Python 3.9"],
      python_requires='>=3.5'
     )