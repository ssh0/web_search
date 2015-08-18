#!/usr/bin/env python
# -*- coding:utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import websearch

if __name__ == '__main__':
    setup(
        name='websearch',
        description='useful GUI tool for web-searching',
        long_description=websearch.__doc__,
        version=websearch.__version__,
        author=websearch.__author__,
        author_email=websearch.__email__,
        license=websearch.__license__,
        url='https://github.com/ssh0/web_search',
        # scripts=['scripts/ranger', 'scripts/rifle'],
        data_files=[('share/doc/websearch', ['README.md']),],
        packages=['websearch']
    )
