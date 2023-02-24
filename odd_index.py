string = input("Enter a string:")
ans = ""
for i in range(len(string)) :
    if i % 2 == 0 :
        ans += string[i]
print(ans)