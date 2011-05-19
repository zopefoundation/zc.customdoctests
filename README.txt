zc.customdoctests -- Use doctest with other languages
*****************************************************

doctest (and recently manuel) provide hooks for using custom doctest
parsers.  zc.customdoctests helps to leverage this to support other
languages, such as JavaScript::

    js> function double (x) {
    ...     return x*2;
    ... }
    js> double(2)
    4

And with `manuel <http://pypi.python.org/pypi/manuel>`_, it
facilitates doctests that mix multiple languages, such as Python,
JavaScript, and sh.

.. contents::

Changes
*******

0.1.0 (2011-05-19)
==================

Initial release
