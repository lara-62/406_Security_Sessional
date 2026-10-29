
import math 

a=2
b=2
P=997
x=0
while True:

    ysquare=x*x*x+a*x+b
    print(math.sqrt(ysquare))
    if math.sqrt(ysquare).is_integer() == True :
        # print(x)
        # print(ysquare)
        break
    else:
        x+=1
        # print(x)
        # print(ysquare)
        if x==1000:
            break