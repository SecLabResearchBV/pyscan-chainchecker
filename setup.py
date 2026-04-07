from pyscan.utils.build_constants import *
from setuptools import setup, find_packages

setup(
    name='pyscan-chainchecker',
    version=VERSION,
    packages=find_packages(),    
    install_requires=['textColor'],
    entry_points = {
        'console_scripts': [CLI_COMMANDNAME + '=pyscan.main:main'],
    }
)
