lam = input("Enter a string:")
lam = lam.lower()
count = 0
for i in lam :
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' :
        count += 1
print(count)