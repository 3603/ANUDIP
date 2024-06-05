num=int(input("enter a number:"))
temp=num
fact=1
while (temp>=1):
    fact=fact*temp
    temp=temp-1
print("factorial of ",num,"=",fact)