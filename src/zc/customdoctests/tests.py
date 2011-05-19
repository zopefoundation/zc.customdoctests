##############################################################################
#
# Copyright (c) 2010 Zope Foundation and Contributors.
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
# from zope.testing import setupstack
# import manuel.capture
# import manuel.doctest
# import manuel.testing
import unittest
import doctest

import zc.customdoctests.js

def custom_doctest_parser():
    r"""
    >>> [e] = zc.customdoctests.DocTestParser().get_examples('''
    ...
    ... >>> 2 + 2 # doctest: +ELLIPSIS
    ... 5
    ...
    ... ''')
    >>> e.source, e.want, e.options == {doctest.ELLIPSIS: True}
    ('2 + 2 # doctest: +ELLIPSIS\n', '5\n', True)

    >>> [e] = zc.customdoctests.DocTestParser(
    ...    ps1='js>', comment_prefix='//', transform=lambda s: 'JS(%r)' % s
    ... ).get_examples('''
    ...
    ... js> 2 +
    ... ... 2 // doctest: +ELLIPSIS
    ... 5
    ...
    ... >>> x
    ... 1
    ...
    ... ''')
    >>> e.source, e.want, e.options == {doctest.ELLIPSIS: True}
    ("JS('2 +\\n2 // doctest: +ELLIPSIS\\n')", '5\n', True)

    """

def test_suite():
    suite = unittest.TestSuite([doctest.DocTestSuite()])
    try:
        import spidermonkey
    except ImportError:
        pass
    else:
        import manuel.capture
        import manuel.doctest
        import manuel.testing
        suite.addTest(
            manuel.testing.TestSuite(
                manuel.doctest.Manuel(parser=zc.customdoctests.js.parser) +
                manuel.doctest.Manuel(parser=zc.customdoctests.js.eq_parser) +
                manuel.doctest.Manuel() +
                manuel.capture.Manuel(),
                'spidermonkey.txt',
                setUp=zc.customdoctests.js.spidermonkeySetUp)
            )
    return suite

