# This is the pip requirements file for extensive
# PyInstaller testing.
#
# Example (assuming current dir is PyInstaller's top-level source dir)::
#
#   python -m pip install -r tests/requirements-libraries.txt  # extensive

# include requirements for base testing
-r requirements-tools.txt


# Needs work
# ----------
# These packages, if updated, produce test failures. Work needs to be done on
# these hooks. Any requirement in this list should be followed by the
# `# pyup: ignore <https://pyup.io/docs/bot/filter/>`_ comment.
#
# - v. 2.2 and above fails.
Django==2.1.8  # pyup: ignore
# - v 3.1.0 fails.
matplotlib==3.0.3  # pyup: ignore
# - v 21.1.0 fails; earlier versions not tested.
keyring==19.2.0  # pyup: ignore


# Working
# -------
# These packages work with no (known) issues.
babel==2.8.0
boto==2.49.0
boto3==1.14.14
botocore==1.17.14
future==0.18.2
gevent==20.6.2
h5py==2.10.0
markdown==3.2.2
phonenumbers==8.12.6
Pillow==7.2.0
pinyin==0.4.0
pycparser==2.20
pycryptodome==3.9.8
pycryptodomex==3.9.8
pyexcelerate==0.9.0
pygments==2.6.1
pylint==2.5.3
PySide2==5.13.0
python-dateutil==2.8.1
pytz==2020.1
pyusb==1.0.2
pyzmq==19.0.1
requests==2.24.0
# simplejson is used for text_c_extension
simplejson==3.17.0
sphinx==2.4.4
# Required for test_namespace_package
sqlalchemy==1.3.18
Unidecode==1.1.1
zeep==3.4.0
zope.interface==5.1.0


# Python 3.5 not supported / supported for older versions
# -------------------------------------------------------
openpyxl==3.0.4; python_version > '3.5'
web3==5.11.1; python_version > '3.5'


# iPython 7.10.0 and higher dropped Python 3.5 support per https://ipython.readthedocs.io/en/stable/whatsnew/version7.html#stop-support-for-python-3-5-adopt-nep-29.
ipython==7.16.1; python_version > '3.5'
ipython==7.9.0; python_version == '3.5'  # pyup: ignore

# pandas 1.0.0 dropped Python 3.5 support.
pandas==1.0.5; python_version > '3.5'
pandas==0.25.3; python_version == '3.5'  # pyup: ignore

# Numpy 1.19 dropped Python 3.5 support
numpy==1.19.0; python_version > '3.5'
numpy<=1.19.0; python_version == '3.5'  # pyup: ignore

# And so did SciPy
scipy==1.5.0; python_version > '3.5'
scipy<=1.5.0; python_version == '3.5'  # pyup: ignore

# Special cases
# -------------
# Wheels are available only on OS X and Win 32. The only Windows 64-bit Python
# tests run are for Python 3.7, so exclude that. There's no way to simply
# exclude Windows 64 bit Python.
pyenchant==3.1.1; sys_platform == 'darwin' or (sys_platform == 'win32' and python_version <= '3.6')

# Per https://www.riverbankcomputing.com/pipermail/pyqt/2020-February/042506.html, Windows PyQt5 5.14.0? and 5.14.1? aren't correctly packaged.
pyqt5==5.13.2; sys_platform == 'win32'
pyqt5==5.14.1; sys_platform != 'win32'
# On Appveyor, newer versions fail with the error message
# ``[1916:2732:0204/144922.809:ERROR:mf_helpers.cc(14)] Error in dxva_video_decode_accelerator_win.cc on line 513``
pyqtwebengine==5.12.1; sys_platform == 'win32'  # pyup: ignore
pyqtwebengine==5.14.0; sys_platform != 'win32'  # pyup: ignore

# uvloop does not currently support Windows.
uvloop==0.14.0; sys_platform != 'win32'
