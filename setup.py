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
name, version = 'zc.customdoctests', '0'

install_requires = ['setuptools']
extras_require = dict(test=['zope.testing', 'python-spidermonkey', 'manuel'])

from setuptools import setup
import os

setup(
    author = 'Jim Fulton',
    author_email = 'jim@zope.com',
    license = 'ZPL 2.1',

    name = name, version = version,
    long_description=(
        open('README.txt').read() + '\n\n' +
        'Detailed dcoumentation\n' +
        '**********************\n\n' +
        open(os.path.join(os.path.dirname(__file__),
                          'src', 'zc', 'customdoctests', 'README.txt')
             ).read() + '\n\n' +
        open(os.path.join(os.path.dirname(__file__),
                          'src', 'zc', 'customdoctests', 'spidermonkey.txt')
             ).read()
        ),
    description = open('README.txt').read().strip().split('\n')[0],
    packages = [name.split('.')[0], name],
    namespace_packages = [name.split('.')[0]],
    package_dir = {'': 'src'},
    install_requires = install_requires,
    zip_safe = False,
    package_data = {name: ['*.txt', '*.test', '*.html']},
    extras_require = extras_require,
    tests_require = extras_require['test'],
    test_suite = name+'.tests.test_suite',
    )
