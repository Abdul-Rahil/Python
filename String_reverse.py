def reverse(lam) :
    if len(lam) == 1:
        return lam
    return reverse(lam[1:])+lam[0]
lam = input("Enter a string:")
print(reverse(lam))

# Without recursion
lam1 = input("Enter a String:")
rev = ""
for i in range(len(lam1)-1,-1,-1):
    rev += lam1[i]
print(rev) 