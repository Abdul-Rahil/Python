m1 = int(input("Enter mass of object1:"))
m2 = int(input("Enter mass of object2:"))
r = int(input("Enter distance between 2 objects"))
G = 6.673*(10**-11)
gf = G*m1*m2 / (r**2)
print("Gravitational force : ",gf)