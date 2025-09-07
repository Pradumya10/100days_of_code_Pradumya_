#print odd no. from n to m .
# Version 1: Using if-else to identify odd/even
n=  int(input("enter starting number  "))
m = int(input("enter ending number "))
for i in range(n , m+1):
    if i%2 ==0:
        print ("even-")
    else:
        print (i,"is an odd no.")
# Version 2: Only print odd numbers
n=  int(input("enter starting number  "))
m = int(input("enter ending number "))
for i in range(n , m+1):
    if i%2 !=0:
        print (i, "is an odd no. ")
   