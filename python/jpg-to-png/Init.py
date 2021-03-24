import os
import sys
import platform

def checkos():

	global sysname

	sysname = platform.system()

	if sysname != 'Windows' and sysname != 'Linux':

		print('Unsupported OS.')
		input('Press Enter to exit: ')
		sys.exit()

	else:

		getreq()

def getreq():

	if sysname == 'Windows':

		os.system('cls')

	else:

		os.system('clear')

	print('Detected ' + sysname + ' Operating System.')
	print()

	print('[*] Installing required modules...')

	if sysname == 'Windows':

		os.system('pip3 install pillow > nul 2>&1')

	else:

		os.system('pip3 install pillow > /dev/null 2>&1')

	print('[*] Creating workspace directories...')

	if sysname == 'Windows':

		os.system('mkdir In-JPG > nul 2>&1')
		os.system('mkdir Out-PNG > nul 2>&1')

	else:

		os.system('mkdir In-JPG > /dev/null 2>&1')
		os.system('mkdir Out-PNG > /dev/null 2>&1')

	print('[*] Verifying installation...')
	print()

	z = checkreq()

	if z == 0:

		print('Workspace was successfully configured!')
		input('Press Enter to exit: ')

	else:

		print('Installation failed.')
		input('Press Enter to exit: ')

	print()
	sys.exit()

def checkreq():

	if sysname == 'Windows':

		x = os.system('python -c \"import PIL\" > nul 2>&1')

	else:

		x = os.system('python3 -c \"import PIL\" > /dev/null 2>&1')

	if x == 0:

		return 0

	else:

		return 1

checkos()
