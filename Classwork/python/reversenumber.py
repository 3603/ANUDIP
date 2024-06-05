n=int(input("enetr a number :")) #number
rev_n=0 #reverse no variable 

while (n!=0):
    temp=n%10
    rev_n=rev_n*10+temp
    n=n//10

print("Reverse string:",rev_n)