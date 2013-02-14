##############################################################################
#
# Copyright (c) Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
import os
from setuptools import setup, find_packages

here = os.path.dirname(__file__)

def read(filename):
    with open(os.path.join(here, filename)) as f:
        return f.read()


install_requires = ['setuptools']

extras_require = dict(
    test=['zope.testing', 'manuel'],
    js=['python-spidermonkey'],
)

setup(
    name='zc.customdoctests',
    version='1.0.1',
    url='http://pypi.python.org/pypi/zc.customdoctests',
    license='ZPL 2.1',
    description=read('README.txt').splitlines(False)[0],
    author='Jim Fulton',
    author_email='jim@zope.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
    ],
    long_description=''.join([
        read('README.txt'),
        '\n\n'
        'Detailed documentation\n'
        '======================\n\n',
        read('src/zc/customdoctests/README.txt'),
        '\n\n',
        read('src/zc/customdoctests/spidermonkey.txt'),
        '\n\n',
        read('CHANGES.txt'),
    ]),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['zc',],
    install_requires=install_requires,
    package_data={'zc.customdoctests': ['*.txt']},
    extras_require=extras_require,
    tests_require=extras_require['test'],
    test_suite='zc.customdoctests.tests.test_suite',
    zip_safe=False,
)
