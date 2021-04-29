n=int(input("Enter the range:"))
sum=0;
x=4; #initialising variable
for i in range(1,n+1):
    sum=(sum+(1/((x)^2)))
    print("1/(%f)^2"%(x),end=" ")
    x=x*2;
    if(n==i):
        print()
    else:
        print("+",end=" ")
print("=",sum)
#code was changed
