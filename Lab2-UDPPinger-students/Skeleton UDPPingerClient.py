# This skeleton is valid for both Python 2.7 and Python 3.
# You should be aware of your additional code for compatibility of the Python version of your choice.

import time
from socket import *

# Get the server hostname and port as command line arguments                    
host = "10.22.76.148"
port = 12000
timeout = 1 # in seconds

server_address = (host, port)
 
# Create UDP client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Note the second parameter is NOT SOCK_STREAM
# but the corresponding to UDP

# Set socket timeout as 1 second
#clientSocket.settimeout(1)

# Sequence number of the ping message
ptime = 0  

# Ping for 10 times
while ptime < 10: 
    ptime += 1
    # Format the message to be sent as in the Lab description	
    data = "Ping"
    
    try:

    	
    	# Record the "sent time"
        st = time.time()
    	# Send the UDP packet with the ping message
        clientSocket.sendto(data, server_address)
    	# Receive the server response
        data, server = clientSocket.recvfrom(1024)
    	# Record the "received time"
        rt = time.time()

        dt = rt - st
    	# Display the server response as an output
        print "Received: %s after %s seconds" %data %dt
     	# Round trip time is the difference between sent and received time

    except:
        # Server does not response
	# Assume the packet is lost
        print("Request timed out.")
        continue

# Close the client socket
clientSocket.close()
 
