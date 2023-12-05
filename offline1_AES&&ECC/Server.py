import socket
import ECC
import AES


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
    Gx=4
    Gy=5
    P=ECC.number.getPrime(128)
    Coefficient=ECC.generateCurve(Gx,Gy,P)
    a=Coefficient[0]
    b=Coefficient[1]
    
    
    # print(a,b,P,Gx,Gy)
    while True :
        c, addr = s.accept()     
        # print ('Got connection from', addr )
        
        # send a thank you message to the client. encoding to send byte type.
         
        
        
        
        
        Ka= ECC.random.randrange(2,P-1)
       

        A=ECC.PointMultiplication(Ka,Gx,Gy,P,a)
        SendShared=str(a)+" "+str(b)+" "+str(P)+" "+str(Gx)+" "+str(Gy)+" "+str(A[0])+" "+str(A[1])
        c.send(SendShared.encode()) 
       
      
        PrivateKey=(c.recv(1024).decode()).split(" ")
       
        Bx=int (PrivateKey[0])
        By=int(PrivateKey[1])
        ## secret key calculation
        # temp=c.recv(1024).decode()
        # temp2=c.recv(1024).decode()
        # Gx=int(temp)
        # Gy=int(temp2)
        SecretA=ECC.PointMultiplication(Ka,Bx,By,P,a)
        # Close the connection with the client 
        key=str(SecretA[0])
        print(key)

        ############################## Encryption ################################
        plaintext=input()
        AES.initKey(key)
        CipherText=AES.CBC_Encryption(plaintext)
        # print(CipherText)
        c.send(CipherText.encode()) 

        c.close()
        
        # Breaking once connection closed
        break
        
server()