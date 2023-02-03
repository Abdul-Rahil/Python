n = int(input("Enter a 3 digit number"))
t = n
num = 0
while t != 0 :
    rem = t % 10
    num += rem**3
    t = t//10
if num == n :
    print("Armstrong number")
else :
    print("Not an armstrong number")