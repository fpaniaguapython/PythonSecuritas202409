class Saldo:
    def __init__(self, saldo_inicial) -> None:
        self.saldo_inicial = saldo_inicial

    def __add__(self, other):
        return self.saldo_inicial + other.saldo_inicial

    def __len__(self):
        return len(str(self.saldo_inicial))


s1 = Saldo(1000)
s2 = Saldo(500)

print(s1 + s2)

print(len(s1))
print(len(s2))