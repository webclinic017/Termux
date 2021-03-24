#!/usr/bin/env python
#-----------------------------------------------------------------------------
# Copyright (c) 2013-2020, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License (version 2
# or later) with exception for distributing the bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#
# SPDX-License-Identifier: (GPL-2.0-or-later WITH Bootloader-exception)
#-----------------------------------------------------------------------------
"""
Prints a list of (maybe) empty hooks.

A hook is listed here if it does not define any of the meaningful
names (eg. hiddenimports). So beside empty hooks, this will print
hooks which import these name from a shared hook (like PIL.Image) or
are calling functions in hookutils.

Proposed usage::

  develutils/find-empty-hooks.py | sort | xargs emacs
  # then in emacs, remove all content in hooks which are realy empty
  # Now delete all hook-files less then 2 bytes in size:
  find PyInstaller/hooks/ -size -2c -print -delete

"""
import glob
import os
import sys

# Expand PYTHONPATH with PyInstaller package to support running without
# installation.
pyi_home = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.insert(0, pyi_home)

import PyInstaller.hooks

hookspath = os.path.dirname(os.path.abspath(PyInstaller.hooks.__file__))

EXPECTED_NAMES = set('hook hiddenimports excludedimports attrs binaries datas'.split())

for hookfilename in glob.glob(os.path.join(hookspath, 'hook-*.py')):
    with open(hookfilename) as fh:
        source = fh.read()
    mod = compile(source, hookfilename, 'exec')
    co_names = set(mod.co_names)
    if co_names.isdisjoint(EXPECTED_NAMES):
        # none of the meaningful names in a hook is here
        print(os.path.relpath(hookfilename, os.getcwd()))
