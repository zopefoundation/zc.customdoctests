Custom doctest parsers
======================

zc.customdoctests provides a little bit of help with creating custom
doctest parsers that work pretty muct like regular doctests, but that
use an alternate means of evaluating examples.  To use it, you call
zc.customdoctests.DocTestParser and pass any of the following options:

ps1
   The first-line prompt, which defaultd to ``'>>>'``.

   This must be a regular expression that matches exact;y 3 characters.

   (Note that you can't override the second-line prompt.)

comment_prefix
   The comment prefix regular expression, which defaults to '#'.

transform
   A function used to transform example source, which defaults to a
   no-operation function.

The js module provides support for using JavaScript in doctests using
`python-spidermonkey
<http://pypi.python.org/pypi/python-spidermonkey>`_. It provides some
examples of defining custom doctest parsers.
