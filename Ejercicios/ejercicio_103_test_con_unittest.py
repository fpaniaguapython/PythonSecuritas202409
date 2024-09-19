import unittest

def sumar(s1 : int, s2 : int) -> int:
    return s1+s2

def restar(s1 : int, s2 : int) -> int:
    return s1+s2

class TestCalculadora(unittest.TestCase):
    def test_1(self):
        resultado = sumar(3,8)
        self.assertEqual(resultado, 11, "La función sumar no ha dado el resultado esperado")

    def test_2(self):
        resultado = restar(3,8)
        self.assertEqual(resultado, -5, "La función restar no ha dado el resultado esperado")

    def test_3(self):
        n1 = 10
        n2 = 8
        if (n1>n2):
            self.fail("Este test hace una evaluación 'programática' de un código")


#Si queremos ejecutar 'manualmente' los test desde cada script
#if __name__=='__main__':
#    unittest.main()

#Si queremos ejecutar 'automáticamente' los test desde consola
#python -m unittest -v .\ejercicio_103_test_con_unittest.py