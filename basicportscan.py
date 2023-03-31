# To create a basic port scanner or we can say a basic nmap scanner first we have to do is to import modules
import sys #This will be used for arguments we can say
import socket # This will be used to create a connection 

if len(sys.argv) == 1: 
    # If user only enters one argument which is file name then we have to give them a hint that what you have to enter.
    print(f"{sys.argv[0]} IP START(opt.) END(opt.)",file=sys.stderr)
    exit(1) # Then we have to give it a time and one second is enough to check that network is available or not
    
ip = sys.argv[1]
start = 1 # Givin it a starting point
end = 65535 # Givin it a ending point

if len(sys.argv) >= 3:
    start = int(sys.argv[2])
    if len(sys.argv) >= 4:
        end = int(sys.argv[3])

# Now we have to create a check port status function and give a returning value as boolean
def CheckPortStatus(port:int) -> bool:
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((ip,port))
        return True
    except (ConnectionRefusedError,socket.timeout):
        return False

# Now we have to create a for loop to check which port is open 
for port in range(start,end):
    response = CheckPortStatus(port)
    if response:
        # If port is open which means we get positive response and by that program will print that which port is open found
        print(f"Open Port Found [{port}]")
        