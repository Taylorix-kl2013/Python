import socket, subprocess, sys
import time 
from progressbar.progressbar import ProgressBar

subprocess.call("exit 1", shell=True)

remoteServer   = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

print ("-" * 60)
print ("Please wait, scanning remote host", remoteServerIP)
print ("-" * 60)



pbar = ProgressBar  # Progressbar can guess maxval automatically.
for i in pbar(range(80)):
    time.sleep(0.01)


try:
    for port in range(1,2000): 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print ("Port {}: \t Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print ("You pressed Ctrl+C")
    sys.exit()
 
except socket.gaierror:
    print ('Hostname could not be resolved. Exiting')
    sys.exit()
 
except socket.error:
    print ("Couldn't connect to server")
    sys.exit()
    
   
print("Scanning completed")

