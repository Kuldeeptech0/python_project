x=int(input("enter a number"))
count=0
i=1
while(i<=x):
    if(x%i==0):
        count=count+1
    i=i+1
if  (count  ==  2):
    print("prime number")

else:
    print("not prime number")

