n = int(input("Enter a number"))
while n != 1 :
    print(n,",",end=" ")
    if n % 2 != 0 :
        n = 3*n+1
    else :
        n = n//2
print(n)
    
