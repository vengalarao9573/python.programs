#program for prime or not
n=int(input("enter a number"))
if n>1:
 for i in range(1, n):
    if (n%i)==0:

       print(n,"is prime")
       break
    else:
         print(n,"not a prime")
else:
    print(n,"is not prime")