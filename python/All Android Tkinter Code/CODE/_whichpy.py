"""
==========================================================================
Demo the code used in Pydroid 3 to determine the running Python,
for use in script spawns in Mergeall, PyEdit's Run "Capture", and 
Frigcal and PyGadgets launchers (the latter two aren't operational).  

Versions 2.2 and 3.0 of Pydroid 3 leave sys.executable empty (a 
bug); both print an empty string for the second output line here
for programs that import the tkinter module (i.e., GUIs).

Pydroid 3 may also locate its Python anywhere from release to release.
Pydroid 3 2.2 and 3.0 located their Pythons at the following paths
(these are their results in the first output line here):

  /data/user/0/ru.iiec.pydroid3/files/arm-linux-androideabi/bin/python
  /data/user/0/ru.iiec.pydroid3/files/aarch64-linux-android/bin/python

The move in 3.0 broke the Mergeall workaround temporarily.  Reading 
a 'which' shell command's result like this is release and path agnostic 
and should suffice for an app with just one Python installed, as long 
as Pydroid 3's shell keeps handling this correctly; else, all bets are 
off until Pydroid 3 fixes this bug.  To see current status, run this 
file in Pydroid 3, and view its main-menu "Graphical program output."

----
**UPDATE, fall 2020**

Pydroid 3 has no real changes log, but sometime around its 4.0 release,
this app WAS FIXED to properly set sys.executable to the running Python 
interpreter's path.  This attribute was left empty in earlier releases
for tkinter GUIs, necessitating the "which" work-around demoed here.

This work-around is harmless, but no longer required--except on devices
running older Pydroid 3 versions without the fix.  For example, "which" 
could be qualified in future versions of patched files here like this:

  import sys, os
  if not sys.executable:
      sys.executable = os.popen('which python').read().rstrip()  # pd3 < 3.02

  # and use sys.executable on all Pydroid 3s

Also note that the Python path move in 3.0 _may_ reflect either Android
NDK changes, or the Android app installer's selection of an ABI-specific 
variant from a fat APK (different devices may imply different paths).  
Either way, this path should be (and now is) stored in sys.executable,
else work-arounds like the "which" here are required.  Expanded coverage:

  https://learning-python.com/mergeall-android-scripts/_README.html#sys.executable

==========================================================================
"""

from tkinter import *
import sys, os

# workaround

wh = os.popen('which python').read().rstrip()  # path to Python executable
print('which=' + repr(wh))

# normal but broken, until Pydroid 3 version 4.0 (ish)

se = sys.executable              # but this is empty - a Pydroid 3 bug in 2.2/3.0
print('\nsys.exe=' + repr(se))   # must use the os.popen() code in this app alone
