#!/data/data/com.termux/files/usr/bin/sh

echo "Python Install"

echo "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects." 

echo "In Termux Python v3.x can be installed by executing"  

pkg install python  

echo "Warning: upgrading major/minor version of Python package, for example from Python 3.8 to 3.9, will make all your currently installed modules unusable. You will need to reinstall them. However upgrading patch versions, for example from 3.8.1 to 3.8.2, is safe." 

echo "Note that Termux does not provide a way for downgrading. If you are not sure whether new Python version is appropriate for you, make a backup of $PREFIX."   

echo "Package management" 

echo "After installing Python, pip package manager will be available. Here is a quick tutorial about its usage" 

echo "Numpy and Scipy" 

echo "Building complex software like numpy and scipy is tedious. Therefore, Termux user its-pointless (aka live_the_dream) has packaged this software and maintain a Termux APT repository with these and many other useful packages." 

echo "Before Numpy/Scipy installation, you need to subscribe to APT repository:"  

curl -LO https://its-pointless.github.io/setup-pointless-repo.sh bash setup-pointless-repo.sh  

echo "Then you can install Numpy or Scipy like a regular Termux package:  

pkg install -y numpy

pkg install -y scipy  

echo "OpenCV" 

echo "Instructions taken from #512 and #1992. OpenCV is not a Python package but it includes the Python bindings (known as opencv-python in pip)." 

echo "OpenCV needs to be built from source using CMake, install it and other dependencies with:  
pkg install build-essential cmake libjpeg-turbo libpng python"  

echo "There might be other required dependecies as well, see the OpenCV docs for the list. 
The rest of the instructions can be copy-pasted straight away, but if you are not sure if you have all dependencies then it might be best to do it in two steps: first all commands up until the LDFLAGS=" -llog" cmake command and then in a second step make and make install." 

echo "To get the sources, git clone (from a suitable folder):"  

cd /sdcard/python/

git clone https://github.com/opencv/opencv

cd opencv  

echo "You should now be in the opencv folder. Let's create a build folder where we will build the package:"

mkdir build

cd build  

echo "To configure the package for python3 but not python2 (change the on/off flags to use python2 instead of python3) we run:"

echo "LDFLAGS=" -llog -lpython3" cmake -DCMAKE_BUILD_TYPE=RELEASE -DCMAKE_INSTALL_PREFIX=$PREFIX -DBUILD_opencv_python3=on -DBUILD_opencv_python2=off -DWITH_QT=OFF -DWITH_GTK=OFF .."

echo "Last command will throw errors if there are missing dependencies. After this we can compile the package with"
  
make  

make install  

Tkinter 

echo "Tkinter is splitted of from the python package and can be installed by"

pkg install python-tkinter  

echo "We do not provide Tkinter for Python v2.7.x. 

echo "Since Tkinter is a graphical library, it will work only if X Windows System environment is installed and running. How to do this, see page Graphical Environment."

echo "Installing Python modules from source" 

echo "Some modules may not be installable without patching. They should be installed from source code. Here is a quick how-to about installing Python modules from source code." 

echo "1. Obtain the source code. You can clone a git repository of your package:"

git clone https://your-package-repo-url cd ./your-package-repo  

echo "2. Optionally, apply the desired changes to source code. There no universal guides on that, perform this step on your own."

echo "3. Optionally, fix the all shebangs. This is not needed if termux-exec is installed and works correctly."

find . -type f -not -path '*/\.*' -exec termux-fix-shebang "{}" \;  

echo "4. Finally install the package:"

python setup.py install
