lam = input("Enter a string:")
n = int(input("Enter the index to be removed:"))
first = lam[:n]
last = lam[n+1:]
print(first+last)