

# Graphical Environment

echo "Termux provides support for programs that use X Window System. However, there no hardware acceleration for rendering and user will have to install a third party application to view graphical output.\n"

echo "To use X11-enabled programs, please, make sure that at least one of the following programs is installed\n"

echo "VNC Viewer - the best choice for interacting with graphical environment. Requires a running VNC server.\n"

echo "XServer XSDL - this one may be unstable but it provides a standalone Xorg server so you don't have to setup VNC.\n"

echo "Enabling the X11 Repository\n"

echo "X11 packages are available in a separate APT repository.\n"

pkg install x11-repo

echo "To disable this repository, you need to uninstall package x11-repo.\n"

echo "Setting up VNC\n"

echo "Server\n"

echo "If you decided to use VNC for graphical output, follow these instructions for properly setting up VNC server.\n"

echo "Install package `tigervnc`\n"

pkg install tigervnc

vncserver -localhost

echo "At first time, you will be prompted for setting up passwords\n"

echo "You will require a password to access your desktops. Password: Verify: Would you like to enter a view-only password (y/n)? n\n"

echo "Note that passwords are not visible when you are typing them and maximal password length is 8 characters.\n"

echo "If everything is okay, you will see this message\n"

echo "\nNew 'localhost:1 ()' desktop is localhost:1 Creating default startup script /data/data/com.termux/files/home/.vnc/xstartup Creating default config /data/data/com.termux/files/home/.vnc/config Starting applications specified in /data/data/com.termux/files/home/.vnc/xstartup Log file is /data/data/com.termux/files/home/.vnc/localhost:1.log\n"

echo "It means that X (vnc) server is available on display 'localhost:1'.\n"

echo "Finally, to make programs do graphical output to the display 'localhost:1', set environment variable like shown here (yes, without specifying 'localhost')\n"

export DISPLAY=":1"

echo "You may even put this variable to your bashrc or profile so you don't have to always set it manually unless display address will be changed.\n"

echo "Client\n"

echo "Here will be assumed that you use this Android VNC client: VNC Viewer (developed by RealVNC Limited).\n"

echo "VNC Viewer: new connection\n"

echo "Determine port number on which VNC server listens. It can be calculated like this: 5900 + {display number}. So for display 'localhost:1' the port will be 5901.\n"

echo "Now open the VNC Viewer application and create a new connection with the following information (assuming that VNC port is 5901)\n"

echo "Address: 127.0.0.1:5901 Name: Termux\n"

echo "Now launch it. You will be prompted for password that you entered on first launch of 'vncserver'. Depending on packages you installed, you may see either entirely black screen or terminal prompt (only if 'aterm' is installed).\n"

echo "Setting up Xserver XSDL\n"

echo "Xserver XSDL setup is nearly same as for VNC. The only differences are that you don't have to configure authentication and variable "DISPLAY" should be set like\n"

echo "export DISPLAY=localhost:0\n"

export DISPLAY=localhost:0

echo "Note that you don't need to set variable "PULSE_SERVER" like application suggests because Termux uses own Pulseaudio package.\n"

echo "Window Managers Installs\n"

echo "Fluxbox Install\n"

echo "Simplest way to get a working graphical environment is to install Fluxbox\n"

pkg install fluxbox

echo "It can be started automatically on VNC server startup. To do this, edit file ~/.vnc/xstartup as shown here\n"

echo "#!/data/data/com.termux/files/usr/bin/sh ## Fluxbox desktop. # Generate menu. fluxbox-generate_menu # Start fluxbox. fluxbox &\n"

echo "Openbox Install\n"

echo "Openbox requires a more complicated configuration than Fluxbox. Firstly you need to install some packages\n"

pkg install openbox pypanel xorg-xsetroot

echo "Put the following lines to your ~/.vnc/xstartup\n"

echo "#!/data/data/com.termux/files/usr/bin/sh # Start Openbox. openbox-session &\n"

echo "Don't put anything else to file ~/.vnc/xstartup but only lines shown above since Openbox has own autostart script. It is located at ${PREFIX}/etc/xdg/openbox/autostart (or alternatively at ~/.config/openbox/autostart). Edit this file like here\n"

echo "# Make background gray. xsetroot -solid gray # Launch PyPanel. pypanel &\n"

echo "Desktop environment (XFCE)\n"

echo "It is possible to setup a full blown desktop environment in Termux. Only XFCE is supported, porting of other environments is not being planned.\n"

echo "Recommended way of installation is through metapackage and not the separate components\n"

pkg install xfce4

echo "VNC server startup configuration (~/.vnc/xstartup) should contain only\n"

echo "#!/data/data/com.termux/files/usr/bin/sh xfce4-session &\n"

echo "Additional recommended packages for installation\n"

netsurf - Simple graphical web browser. Javascript is not supported.

echo "xfce4-terminal - Terminal emulator for XFCE. It is not included as part of XFCE installation to allow use of aterm or st."
