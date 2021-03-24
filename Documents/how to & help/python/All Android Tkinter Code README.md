#### This file documents recent release changes, and includes general 
file install and upgrade notes.

---

  PyEdit:
    -textEditor.py (work around Pydroid 3 3.0 webbrowser bugs: Help + Run Code)

  Mergeall:
    -launch-mergeall-GUI.pyw (work around Pydroid 3 3.0 webbrowser bugs: Help + logfiles)

  Frigcal 
    - frigcal.py (work around Pydroid 3 3.0 webbrowser bugs: Help)

  Frigcal's and PyGadgets' launcher scripts were also modified for the same 
  help workarounds but are not fully operational, and need not be reinstalled.
  PyGadgets' launcher now also works around Pydroid 3's button color-loss bug.
    - frigcal-launcher.pyw
    - PyGadgets.py

  The _openbrowser.py and _whichpy.py demo scripts were also updated, but
  are not required to run application programs.

---

# SOURCE-CODE FILES CHANGED APRIL 19, 2019
Only the first two are required reinstalls, for the latest Pydroid 3

  PyEdit:
    -textEditor.py (handle Pydroid 3 3.0's new Python path in Run Code)

  Mergeall:
    -launch-mergeall-GUI.pyw (handle Pydroid 3 3.0's new Python path in merge spawn)
    -mergeall_configs.py     (logfile documentation change only: optional reinstall)

  The following file was also changed (to use webbrowser), but its 
  changes did not alter behavior, and it need not be reinstalled:
    - frigcal.py

  Frigcal's and PyGadgets' launcher scripts were also modified, 
  but are not fully operational, and need not be reinstalled:
    - frigcal-launcher.pyw
    - PyGadgets.py

  PyCalc also opens its "hist" history display a few characters wider
  for ease of use (and small phones have room), but this is trivial:
    - calculator.py

New here are _openbrowser.py that demos web-browser opening techniques
and _whichpy.py that demos a sys.executable workaround technique, and
_font-tests-pydroid3.py was updated with new information.  These three
files are never required to run application programs.

---

# All have multiple improvements, and are strongly suggested reinstalls

  Frigcal:
    -frigcal.py
    -frigcal_configs.py

  PyCalc:
    -calculator.py
    -helpmessage.py

  PyEdit:
    -textEditor.py

  Mergeall:
    -launch-mergeall-GUI.pyw

  PyPhoto, PyClock, PyToe: 
    - also use the new helpmessage.py

For earlier changes, see patched files' Android preambles.

---

# HOW TO USE CHANGED FILES:

  If installing for the first time, simply follow the guide's instructions. 
  If upgrading, re-move/re-copy the files above into each program's folder.
  If you've made changes to a configurations file (e.g., frigcal_configs.py),
  be sure to save and re-add them to the new version.

  Caution: when upgrading to a new version of a changed file, copies in some 
  Android file explorers may store the new version alongside the old with a 
  "_1" name pattern, which means it will not be used by the program; remove 
  prior versions manually if needed, or move instead of copying.  This may 
  be an issue if you don't get an "overwrite" dialog from your file explorer.

---

# GENERAL NOTES ON CHANGES:

  For more details on changes, see changed code files, and their programs' 
  Usage Notes in the following document:

    https://learning-python.com/using-tkinter-programs-on-android.html
 
  In general, the latest version of a patched source-code file contains 
  all changes to date, and every file includes an Android preamble that 
  documents recent-changes' purpose and date for every release in which 
  it was changed; check these periodically for programs you use.

---

# About Mergeall file copies:

  The changed Mergeall files in this folder:

    launch-mergeall-GUI.pyw
    mergeall_configs.py

  are redundant copies of those in the Mergeall package here:

    https://learning-python.com/mergeall-android-scripts/

  See that package's documentation for more details at:

    https://learning-python.com/mergeall-android-scripts/_README.html#toc83

  Some screenshots in .. are copied from the Mergeall package too;
  redundancy is a bad idea in general, but it's a convenience here.

---

### Also included is _android_test.py to simplify platform testing in code that must vary on Android (e.g., font configs), and other test programs named with a leading "_" character.

#### File ALL-ANDROID-TKINTER-CODE.zip contains all the files here, for copying to your phone in a single step.

#### SEE ALSO: file _changes-and-upgrades.txt here includes a list of 
code files recently changed, and extra install/upgrade instructions.

---

#### This folder has changed source code files to copy into your various unzipped source-code packages, per the instructions in the guide here:

  http://learning-python.com/using-tkinter-programs-on-android.html

---
