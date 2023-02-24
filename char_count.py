def char_count(string,ch) :
    if len(string) == 0 :
        return 0
    elif string[0] == ch :
        return 1+char_count(string[1:],ch)
    else :
        return char_count(string[1:],ch)
lam = input("Enter a string:")
ch = input("Enter the character to be counted:")
print(char_count(lam,ch))
