import socket
import random

from BitVector import *

from Crypto.Util import number

import ECC
def main():
    # Create a socket object 
    s = socket.socket()         
    
    # Define the port on which you want to connect 
    port =3000             
    
    # connect to the server on local computer 
    s.connect(('127.0.0.1', port)) 
    
    # receive data from the server and decoding to get the string.
    print (s.recv(1024).decode())
    print (s.recv(1024).decode())
    # close the connection 
    s.close() 
    

main()    