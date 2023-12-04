
import random

from BitVector import *

from Crypto.Util import number

# Generate the shared parameters G, a, b, and P 





def PointMultiplication(Ka,Gx,Gy,P,a):
############## Double and Add algorithm for point Multiplication ##################

    BitsOfKa=BitVector(intVal=Ka)
    print(BitsOfKa)


    # for i in range(len(BitsOfKa)):
    #     print(BitsOfKa[i])


    ###### For all other bits without Msb:  1-> doubling and addition and 0-> only doubling ######

    Px=Gx
    Py=Gy
    print(Gx)
    print(Gy)
    for i in range (1,len(BitsOfKa)):
        s1=(3*pow(Px,2)+a)%P
        s2=pow(2*Py,-1,P)
        s=(s1*s2)%P
        tempx=(pow(s,2)-(2*Px))%P
        Py=(s*(Px-tempx)-Py)%P
        Px=tempx
        if BitsOfKa[i]==1:
            s1=(Py-Gy)%P
            print(Px-Gx)
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
        print(a)
        RightSide=(Gx*Gx*Gx)+a*Gx
        b=modulus-RightSide
        if ((4*(a*a*a)+27*(b*b))%P) !=0:
            break

    return a, b


    

def main():

    #hardcoding these parameters

    a=2
    b=2
    P=17
    Gx=4
    Gy=5

    #this elliptic curve order #E

    E=19
    P=number.getPrime(128)
    # print(P)
    # #curve generation
    Coefficient=generateCurve(Gx,Gy,P)
    a=Coefficient[0]
    b=Coefficient[1]
    # print(b)
    Ka= random.randrange(2,P-1)
    print(Ka)
    Kb=random.randrange(2,P-1)
    print(Kb)
    

    A=PointMultiplication(Ka,Gx,Gy,P,a)
    B=PointMultiplication(Kb,Gx,Gy,P,a)

    print(A[0])
    print(A[1])

    print(B[0])
    print(B[1])
    
    ## secret key calculation
    Gx=B[0]
    Gy=B[1]
    SecretA=PointMultiplication(Ka,Gx,Gy,P,a)

    Gx=A[0]
    Gy=A[1]
    SecretB=PointMultiplication(Kb,Gx,Gy,P,a)
    print(SecretA)
    print(SecretB)
    # print((Ka*B[0])%P)
    # print((Kb*A[0])%P)

main()
# y1=input()
# p=input()
# result=pow(int(y1),-1,int(p))

# print(result)
