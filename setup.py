#-*- coding: utf-8 -*-

"""
    waltz
    ~~~~~

    Setup
    `````

    $ pip install waltz    
"""

from distutils.core import setup
import os

setup(
    name='p2c2',
    version='0.0.1',
    url='http://github.com/mekarpeles/practical-python_ebook',
    author='mek',
    author_email='michael.karpeles@gmail.com',
    packages=[
        'subapps',
        'routes',
        'configs',
        ],
    platforms='any',
    license='LICENSE',
    install_requires=[
        'waltz >= 0.1.68',
    ],
    description="Practical Python, Creative Commons (P2C2)",
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
)
