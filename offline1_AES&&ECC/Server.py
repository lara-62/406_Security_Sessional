import socket



def server():
    s=socket.socket()
    print("Socket successfully created")
    port = 3000
    s.bind(('',port))
    print ("socket binded to %s" %port)
    s.listen(5)     
    print ("socket is listening") 
    
    while True :
        c, addr = s.accept()     
        print ('Got connection from', addr )
        
        # send a thank you message to the client. encoding to send byte type.
         
        c.send('Thank you for connecting'.encode()) 
        
        c.send('\nNow get lost'.encode())
        
        # Close the connection with the client 
        c.close()
        
        # Breaking once connection closed
        break
        
server()