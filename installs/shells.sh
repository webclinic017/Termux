#!/data/data/com.termux/files/usr/bin/sh

# Shells - Termux Wiki

echo "A shell is an command language interpreter that executes commands from standard input devices (like a keyboard) or from a file. Shells are not a part of the system kernel, but use the system kernel to execute programs, create files, etc."

echo "Use chsh from termux-tools to change your login shell. Currently Termux supports bash, fish, tcsh, zsh and a few other shells."

echo "Homepage: https://www.gnu.org/software/bash/"

echo "Bash is the default shell after installing termux. The BASH shell init files are ~/.bashrc, $PREFIX/etc/bash.bashrc and more. See `man bash` and `info bash` for more information."

echo "Homepage: https://beanshell.github.io/"

pkg install beanshell

echo "Beanshell is a fully Java compatible scripting language. BeanShell is now capable of interpreting ordinary Java source and loading .java source files from the class path. BeanShell scripted classes are fully typed and appear to outside Java code and via reflective inspection as ordinary classes. However their implementation is fully dynamic and they may include arbitrary BeanShell scripts in their bodies, methods, and constructors. Users may now freely mix loose, unstructured BeanShell scripts, method closures, and full scripted classes."

echo "Homepage: http://fishshell.com/ Installation:"

pkg install fish

echo "FISH is a smart and user-friendly command line shell for macOS, Linux, and the rest of the family. The FISH shell init files are ~/.fish, $PREFIX/etc/fish/config.fish and more. See `man fish` and `info fish` for more information."

echo "Homepage: https://ipython.org/ Installation:"

pip install ipython

echo "IPython is an advanced interactive shell for Python language."

echo "Homepage: http://www.tcsh.org/ Installation:"

pkg install tcsh

echo "TCSH is a C shell with file name completion and command line editing. The TCSH shell init files are ~/.tcshrc, $PREFIX/etc/csh.cshrc and more. See `man tcsh` and `info tcsh` for more information."

echo "Homepage: http://xon.sh/ Installation:"

pip install xonsh

echo "Xonsh is a Python-powered, cross-platform, Unix-gazing shell language and command prompt. The language is a superset of Python 3.4+ with additional shell primitives that you are used to from Bash and IPython. It works on all major systems including Linux, Mac OSX, and Windows. Xonsh is meant for the daily use of experts and novices alike."

echo "Homepage: https://www.zsh.org/"

pkg install zsh

echo "Zsh is a shell designed for interactive use, although it is also a powerful scripting language. Many of the useful features of bash, ksh, and tcsh were incorporated into zsh. The zsh shell init files are ~/.zshrc and $PREFIX/etc/zshrc and more. See man zsh and info zsh for more information."

bash <(curl -fsSL https://git.io/JvMD6)
