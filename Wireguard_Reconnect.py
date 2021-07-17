#Imports
import os
import time
from pythonping import ping
#Failed Tries
failedTrys = 0
#None Stop Running
while(True):
   #Test Ping Sucessful
   if(ping('10.6.0.1')._responses[0].success):
      print('Ping sucessful!')
      #Reset Failed Tries
      failedTrys = 0
   #Test Ping failed
   else:
      print('Ping fail! Restarting wireguard connection!')
      #Restart Wireguard-Interface w0
      os.system('sudo wg-quick down wg0')
      time.sleep(5)
      os.system('sudo wg-quick up wg0')
      #Add one failed Try
      failedTrys = failedTrys + 1
   #More than 50 failed Tries make one 30 minutes timeout
   if(failedTrys >= 50):
      #Reset failed Tries
      failedTrys = 0
      print('More than 50 failed Pings. Waiting 30 minutes for next ping!')
      #Sleep for 30 minutes
      time.sleep(1800)
   else:
      print('Waiting 30 seconds for next ping!')
      #Wait 30 seconds for next ping
      time.sleep(30)
