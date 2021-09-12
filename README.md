<h1>python_wireguard_auto_reconnect</h1>

This Python program  checks if a wireguard connection is still alive and restarts if the connection is lost.
The program in the specific case is for Linux. 

<h2>Installation of needed Python Modules:</h2>
sudo pip/pip3 install pythonping

<h2>Additional notes:</h2>
- If you want to use it on another operating system you only have to change the line "os.system('sudo wg-quick down wg0')" and "os.system('sudo wg-quick up wg0').
<br>
- Other values like the timeouts can be adjusted as well.
<br>
- The program must always be run with elevated privileges because of the package pythonping.
