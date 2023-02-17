n = int(input("Enter a number:"))
count = 0
while n :
    n &= n-1
    count += 1
print("No.of set bits ",count)