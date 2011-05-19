##############################################################################
#
# Copyright (c) 2011 Zope Foundation and Contributors.
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

import doctest
import re
import sys

class DocTestParser(doctest.DocTestParser):
    "Doctest parser that creates calls into JavaScript."

    def __init__(self, *args, **kw):
        ps1 = kw.pop('ps1', '>>>')
        comment_prefix = kw.pop('comment_prefix', '#')
        self.transform = kw.pop('transform', lambda s: s)
        getattr(doctest.DocTestParser, '__init__', lambda : None)(*args, **kw)

        self._EXAMPLE_RE = re.compile(
            r'''
            # Source consists of a PS1 line followed by zero or more PS2 lines.
            (?P<source>
                (?:^(?P<indent> [ ]*) %(ps1)s    .*)    # PS1 line
                (?:\n           [ ]*  \.\.\.     .*)*)  # PS2 lines
            \n?
            # Want consists of any non-blank lines that do not start with PS1.
            (?P<want> (?:(?![ ]*$)        # Not a blank line
                         (?![ ]*%(ps1)s)  # Not a line starting with PS1
                         .*$\n?           # But any other line
                      )*)
        ''' % dict(ps1=ps1), re.MULTILINE | re.VERBOSE)

        self._OPTION_DIRECTIVE_RE = re.compile(
            comment_prefix +r'\s*doctest:\s*([^\n\'"]*)$', re.MULTILINE)



    def parse(self, string, name='<string>'):
        r =doctest.DocTestParser.parse(self, string, name)
        for s in r:
            if isinstance(s, doctest.Example):
                s.source = self.transform(s.source)
        return r
