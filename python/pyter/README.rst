=====
pyter
=====

pyter is a simple Translation Error Rate evaluation command.

Currentry under development state.

============
Installation
============
::

  pip install pyter

or checkout the repository::

  git clone git://github.com/aflc/pyter.git
  cd pyter
  pip install -e .


=====
Usage
=====

------------------------------
In Python code(Python2.x case)
------------------------------
import

>>> import pyter

To get a TER score, both hypothesis sentence and reference sentence have to a list of word.

>>> ref = u'SAUDI ARABIA denied THIS WEEK information published in the AMERICAN new york times'.split()
>>> hyp = u'THIS WEEK THE SAUDIS denied information published in the new york times'.split()
>>> '%.3f' % pyter.ter(hyp, ref)
'0.308'

If you want to use a character based matching, write a code like that.

>>> ref = list(u"Pythonは、より素早く、効果的にシステムとの統合が可能なプログラミング言語です。")
>>> hyp = list(u"Pythonは、より迅速に動作するとより効果的にシステムを統合できるプログラミング言語です。")
>>> '%.3f' % pyter.ter(hyp, ref)
'0.357'

----------------------
Command line interface
----------------------
Please type::

  pyter --help


===========
ReleaseNote
===========

v0.2.2.1
   * bugfix release

v0.2.2
   * fixed #1, invalid scoreing.

v0.2.1
   * New CLI interface
   * Refactoring the whole code
   * **This version is incompatible with the previous version.**
v0.2
   * Replace normal DP based edit distance with cached version. A little performance improvement.
v0.1.1
   * Minor fix, and register to PyPi
v0.1
   * Initial release

=======
License
=======

It is released under the MIT license.

    Copyright (c) 2011 Hiroyuki Tanaka
    
    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
