import socket
import random

from BitVector import *

from Crypto.Util import number

import ECC
import AES
def main():
    # Create a socket object 
    s = socket.socket()         
    
    # Define the port on which you want to connect 
    port =3000             
    
    # connect to the server on local computer 
    s.connect(('127.0.0.1', port)) 
    
    # receive data from the server and decoding to get the string.
    # a=2
    # b=2
    # P=17
    # Gx=4
    # Gy=5

    ReceivedShared=(s.recv(1024).decode()).split(" ")
    # print(ReceivedShared)
    a=int(ReceivedShared[0])
    b=int(ReceivedShared[1])
    P=int(ReceivedShared[2])
    Gx=int(ReceivedShared[3])
    Gy=int(ReceivedShared[4])
    Ax=int (ReceivedShared[5])
    Ay=int(ReceivedShared[6])
    # print(a,b,P,Gx,Gy,Ax,Ay)
    Kb=random.randrange(2,P-1)
    # print(Kb)
    B=ECC.PointMultiplication(Kb,Gx,Gy,P,a)
    # print(B[0])
    # print(B[1])
    
    PrivateKey=str(B[0])+" "+str(B[1])
    s.send(PrivateKey.encode()) 
   
    SecretB=ECC.PointMultiplication(Kb,Ax,Ay,P,a)
    # print(SecretB)
    # close the connection 
    s.close() 
    

main()    