import setuptools
from setuptools import find_packages
from numpy.distutils.core import setup
from numpy.distutils.core import Extension
from numpy.distutils import log
import re, os

packages = find_packages(exclude=('tests', 'doc'))
provides = ['taurex_offset', ]

requires = []

install_requires = ['taurex']

entry_points = {'taurex.plugins': 'taurex_offset = taurex_offset'}

setup(name='taurex_offset',
      author="Quentin Changeat",
      author_email="tbd",
      license="BSD",
      description='Add multiple spectra and offset fitting to TauREx 3.1',
      packages=packages,
      entry_points=entry_points,
      provides=provides,
      requires=requires,
      install_requires=install_requires)