def sumar(s1 : int, s2 : int) -> int:
    assert(isinstance(s1, int) and isinstance(s2, int))
    return s1+s2

print(sumar(3,2))#OK
print(sumar('a',2))#KO