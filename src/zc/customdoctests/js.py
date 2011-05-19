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
import os
import re
import sys
import zc.customdoctests

run_time = None

def transform(s, f='JS'):
    if s[-1] == '\n':
        return (r'%s(r"""%s"""+"\n")' % (f, s)) + '\n'
    else:
        return r'%s(r"""%s""")' % (f, s)

parser = zc.customdoctests.DocTestParser(
    ps1='js>', comment_prefix='//', transform=transform)

# parser_ is like parser, except adds: var _ = to
# the fron of the executed code.
eq_parser = zc.customdoctests.DocTestParser(
    ps1='js!', comment_prefix='//',
    transform=lambda s: transform(s, 'JS_'))


# spidermonkey hacks below:

class JavaScriptError(Exception):

    def __str__(self):
        try:
            return "%s\nJS Traceback:%s" % (
                self.args[0].message,
                '\n'.join(reversed(self.args[0].stack.split('\n')))
                )
        except:
            return str(self.args[0])


class ContextConvenience(object):

    def __init__(self, context):
        object.__setattr__(self, '_context', context)

    def __getattr__(self, name):
        return self._context.execute(name)

    def __setattr__(self, name, v):
        self._context.add_global(name, v)

    def __call__(self, src):
        self._context.execute(load_template % src)
        if self.spidermonkey_error is not None:
            raise JavaScriptError(self.spidermonkey_error)

def spidermonkeySetUp(test_or_self=None):
    global run_time
    if run_time is None:
        import spidermonkey
        run_time = spidermonkey.Runtime()
    cx = run_time.new_context()
    JS = cx.execute

    js = ContextConvenience(cx)

    if test_or_self is not None:
        globs = getattr(test_or_self, 'globs', test_or_self.__dict__)
        globs['JS'] = JS
        globs['JS_'] = js
        globs['js'] = js
        globs['add_js_global'] = cx.add_global

    def load_(name):
        if name.startswith('file://'):
            name = name[7:]
        return JS(load_template % open(name).read(), name)

    # Rhino & spidermonkey/js compatability functions
    cx.add_global('python', dict(
        os = os,
        open = open,
        ))
    cx.add_global('load_', load_)
    JS(load_js)
    cx.add_global('print',
                  lambda *s: sys.stdout.write(('%s\n' % ' '.join(map(unicode, s))).encode('utf-8'))
                  )
    cx.add_global('printe',
                  lambda *s: sys.stderr.write('%s\n' % ' '.join(map(unicode, s)))
                  )
    return js


load_template = ("spidermonkey_error = undefined; "
                 "try { %s } catch (e) {spidermonkey_error = e;}")

load_js = """
function load(p) {
    if (p.slice(0, 7) == 'file://') {
        p = p.slice(7);
    }
    try { console.debug('loading', p); } catch (e) {}
    if (! python.os.path.exists(p)) {
        throw "Doesn't exist: "+p;
    }
    var result = load_(p);
    if (spidermonkey_error) {
        throw spidermonkey_error;
    }
    return result;
}
"""
