import os
from setuptools import setup, find_packages
PACKAGES = find_packages()

opts = dict(name='dockme',
            maintainer='Koshlan Mayer-Blackwell',
            maintainer_email='kmayerbl@fredhutch.org',
            description='Package for learning how to containerize',
            url='https://github.com/kmayerbl/dockme',
            version='0.1',
            packages=PACKAGES)

if __name__ == '__main__':
    setup(**opts)