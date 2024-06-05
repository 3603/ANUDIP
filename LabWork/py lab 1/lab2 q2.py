n=int(input("enetr a number :")) #number
num=n#thsi stores n value used for checking later 
rev_n=0 #reverse no variable 

while (n!=0):
    temp=n%10
    rev_n=rev_n*10+temp
    n=n//10
print("Reverse string:",rev_n)

if (num==rev_n):
    print("Number is plaindrome")
else:
    print("Number is not plaindrome")    

