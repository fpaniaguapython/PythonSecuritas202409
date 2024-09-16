s1 = "Me gustan los lunes"
s2 = "Me gustan los lunes"

print(id(s1))
print(id(s2))
print(id(s1)==id(s2))#True

s1 = "Me gustan los lunes"
s2 = "No me gustan los lunes"

print(id(s1))
print(id(s2))
print(id(s1)==id(s2))#False

s2 = s1

print(id(s1))
print(id(s2))
print(id(s1)==id(s2))#True