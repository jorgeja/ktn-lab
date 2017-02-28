# This skeleton is valid for both Python 2.7 and Python 3.
# You should be aware of your additional code for compatibility of the Python version of your choice.

import time
from socket import *

# Get the server hostname and port as command line arguments                    
host = '10.24.38.2' # FILL IN START		# FILL IN END
port = 9999 # FILL IN START		# FILL IN END
timeout = 3 # in seconds
 
# Create UDP client socket
# FILL IN START		
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Note the second parameter is NOT SOCK_STREAM
# but the corresponding to UDP

# Set socket timeout as 1 second
clientSocket.settimeout(1)

# FILL IN END

# Sequence number of the ping message
ptime = 0  

# Ping for 10 times
while ptime < 10: 
    ptime += 1
    # Format the message to be sent as in the Lab description	
    data = "Ping " + str(ptime) + " " # FILL IN START		# FILL IN END
    
    try:
    	# FILL IN START
    	
        # Record the "sent time"
        sentTime = time.time()
        data += str(sentTime)
        # Send the UDP packet with the ping message
        clientSocket.sendto(data, (host, port))
        # Receive the server response
        message, address = clientSocket.recvfrom(2048)  
        # Record the "received time"
        recieveTime = time.time()
        # Display the server response as an output
        print message
        # Round trip time is the difference between sent and received time
        RTT = recieveTime - sentTime
        RTT = RTT * 1000
        print "RTT: " + str(RTT)        
        # FILL IN END
    except:
        # Server does not response
	# Assume the packet is lost
        print("Request timed out.")
        continue

# Close the client socket
clientSocket.close()
 
