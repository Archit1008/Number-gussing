import random as ra
print("computer gussing number")
n=ra.randrange(1,100)
print("now please enter number")
f=int(input())
t=0
while(f!=n):
        if(f < n):
              print("enter more  number as  compare to previous number")
              f=int(input())
        elif (f>n):
              print("enter less  number as compare to previous number")
              f=int(input())
        t=t+1
print("your rank is",t,'now game over')


