a=int(input("print table 1 to x[enter value of x]]="))
i=1
while(i<=a):
    for j in range (1,11):
        print(i,"x",j,"=",i*j)
    print("---------")
    i=i+1