import math
print("Enter the values of coefficient in a*x^3 + b*x^2 + c*x + d:")
arr = []
for i in range(0,4) :
    m = int(input())
    arr.append(m)
x = int(input("Enter the value of x :"))
sum = 0
j = 3
for i in range(0,4) :
    sum += arr[i]*math.pow(x,j)
    j -= 1
print("result :",sum)

