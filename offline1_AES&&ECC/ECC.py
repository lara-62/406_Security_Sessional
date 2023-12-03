
import random

from BitVector import *

# Generate the shared parameters G, a, b, and P 

#hardcoding these parameters

a=2
b=2
P=17
Gx=5
Gy=1

#this elliptic curve order #E

E=19
Ka= random.randrange(2,E)
print(Ka)


Kb=random.randrange(2,E)

print(Kb)


############## Double and Add algorithm for point Multiplication ##################

BitsOfKa=BitVector(intVal=Ka)
print(BitsOfKa)


# for i in range(len(BitsOfKa)):
#     print(BitsOfKa[i])


###### For all other bits without Msb:  1-> doubling and addition and 0-> only doubling ######

Px=Gx
Py=Gy

for i in range (1,len(BitsOfKa)):
    s1=(3*pow(Px,2)+a)%P
    s2=pow(2*Py,-1,P)
    s=(s1*s2)%P
    tempx=(pow(s,2)-(2*Px))%P
    Py=(s*(Px-tempx)-Py)%P
    Px=tempx
    if BitsOfKa[i]==1:
        s1=(Py-Gy)%P
        s2=pow((Px-Gx),-1,P)
        s=(s1*s2)%P
        tempx=(pow(s,2)-Px-Gx)%P
        Py=(s*(Gx-tempx)-Gy)%P
        Px=tempx


print(Px)
print(Py)
    





# y1=input()
# p=input()
# result=pow(int(y1),-1,int(p))

# print(result)
