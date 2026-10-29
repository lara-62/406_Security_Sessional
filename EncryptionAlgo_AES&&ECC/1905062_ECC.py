
import random

from BitVector import *

from Crypto.Util import number

import time

# Generate the shared parameters G, a, b, and P 





def PointMultiplication(Ka,Gx,Gy,P,a):
############## Double and Add algorithm for point Multiplication ##################

    BitsOfKa=BitVector(intVal=Ka)
    # print(BitsOfKa)


    # for i in range(len(BitsOfKa)):
    #     print(BitsOfKa[i])


    ###### For all other bits without Msb:  1-> doubling and addition and 0-> only doubling ######

    Px=Gx
    Py=Gy
    # print(Gx)
    # print(Gy)
    for i in range (1,len(BitsOfKa)):
        s1=(3*pow(Px,2)+a)%P
        s2=pow(2*Py,-1,P)
        s=(s1*s2)%P
        tempx=(pow(s,2)-(2*Px))%P
        Py=(s*(Px-tempx)-Py)%P
        Px=tempx
        if BitsOfKa[i]==1:
            s1=(Py-Gy)%P
            # print(Px-Gx)
            s2=pow((Px-Gx),-1,P)
            s=(s1*s2)%P
            tempx=(pow(s,2)-Px-Gx)%P
            Py=(s*(Gx-tempx)-Gy)%P
            Px=tempx
    # print(Px)
    # print(Py)
    return Px ,Py
        
    
def generateCurve(Gx,Gy,P):
   
    #y^2= (x^3 + ax +b) mod p

    modulus=(Gy*Gy)%P
    
    while True:
        a=random.randint(0,P-1)
        # print(a)
        RightSide=(Gx*Gx*Gx)+a*Gx
        b=modulus-RightSide
        if ((4*(a*a*a)+27*(b*b))%P) !=0:
            break

    return a, b


    

if __name__ == "__main__":

    
    keylen=[128,192,256]

    a=2
    b=2
    P=17
    Gx=4
    Gy=5
    
    print("key length            time for A              time for B              time for Shared Secretekey")
    
    for i in range(len(keylen)):
        AvgtimeA=0
        AvgtimeB=0
        AvgtimeShared=0
        for j in range(0,5):

            P=number.getPrime(keylen[i])
            Coefficient=generateCurve(Gx,Gy,P)
            a=Coefficient[0]
            b=Coefficient[1]
            Ka= random.randrange(2,P-1)
            Kb=random.randrange(2,P-1)
            timeA=time.time()
            A=PointMultiplication(Ka,Gx,Gy,P,a)
            AvgtimeA+= time.time()-timeA
            timeB=time.time()
            B=PointMultiplication(Kb,Gx,Gy,P,a)
            AvgtimeB+= time.time()-timeB
            Gx=B[0]
            Gy=B[1]
            timeShared=time.time()
            SecretA=PointMultiplication(Ka,Gx,Gy,P,a)
            AvgtimeShared+=time.time()-timeShared
            Gx=A[0]
            Gy=A[1]
            SecretB=PointMultiplication(Kb,Gx,Gy,P,a)
            # print(SecretA)
            # print(SecretB)
        AvgtimeA=((AvgtimeA/5)*1000)
        AvgtimeB=((AvgtimeB/5)*1000)
        AvgtimeShared=((AvgtimeShared/5)*1000)
        print(keylen[i],"                  %.2fms                   %.2fms                 %.2fms             " % (AvgtimeA , AvgtimeB  , AvgtimeShared))
