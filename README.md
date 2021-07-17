This is a Python program that checks if a wireguard connection still exists and restarts if the connection is lost.

The program in the specific case is for Linux. If you want to use it on another operating system you only have to change the line "os.system('sudo wg-quick down wg0')" and "os.system('sudo wg-quick up wg0').

Other values like the timeouts can be adjusted as well.

The program must always be run with elevated privileges because of the package pythonping.

Prerequisites:

sudo pip3 install pythonping or sudo pip install pythonping.

