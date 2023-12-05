import socket
import ECC
import AES

import random

def server():
    s=socket.socket()
    # print("Socket successfully created")
    port = 3000
    s.bind(('',port))
    # print ("socket binded to %s" %port)
    s.listen(5)     
    # print ("socket is listening") 
    a=2
    b=2
    P=17
    Gx=random.randint()
    Gy=5
    Coefficient=generateCurve(Gx,Gy,P)
    a=Coefficient[0]
    b=Coefficient[1]
    SendShared=str(a)+" "+str(b)+" "+str(P)+" "+str(Gx)+" "+str(Gy)
    print(SendShared)
    while True :
        c, addr = s.accept()     
        print ('Got connection from', addr )
        
        # send a thank you message to the client. encoding to send byte type.
         
        
        
        c.send(SendShared.encode()) 
        
        c.send('\nNow get lost'.encode())
        
        # Close the connection with the client 
        c.close()
        
        # Breaking once connection closed
        break
        
server()