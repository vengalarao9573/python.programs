#reverse a number
n=int(input("enter a any four digit number:"))
rev=0
while n>0:
    r=n%10
    n=n//10
    rev=(rev*10)+r
print(rev)

