<h1>python_wireguard_auto_reconnect</h1>

<h2>Description of the project</h2>
This Python program  checks if a wireguard connection is still alive and restarts if the connection is lost.<br>
The programm is constantly pinging the vpn-gateway. <br>
If the ping is a successful the programm goes to sleep for a 30 seconds and than pings again.<br>
If the ping fails the programm restarts the wireguard connection and than pings again. After 50 failed tries the programm is timeouted for 30 minutes. <br>

<h2>Project status</h2>
The project itself is complete and ready for use. I am open for improvments.

<h2>Requirements</h2>
Requirements for running the webui are:
- python (3.x.x) <br>
- pip (v3) or any other packetmanager <br>
- pythonping

<h2>Installation</h2>
1. Download and Install Python. <br>
For windows go to (https://www.python.org/downloads/) <br>
For linux use <code> sudo apt-get install python3.x </code> <br>
2. Download and install pip-packetmanager <br>
3. Install pythonping <br>
For Windows <code> py -3 -m pip install pythonping </code> <br>
For Linux <code> pip3 install pythonping </code> <br>
4. Now run the Wireguard_Reconnect.py - File
For Windows <code> py -3 Wireguard_Reconnect.py </code> <br>
For Linux <code> python3 Wireguard_Reconnect.py </code> <br>

<h2>Additional notes:</h2>
- If you want to use it on another operating system you only have to change the line "os.system('sudo wg-quick down wg0')" and "os.system('sudo wg-quick up wg0').<br>
- Other values like the timeouts can be adjusted as well. <br>
- The program must always be run with elevated privileges because of the package pythonping.
