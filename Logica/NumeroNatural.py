class NumeroNegativoException(Exception):
    pass

class NumeroNatural():
    def validarTipo(self):
        while True:
            try:
                self.numeroNatural = int(input("Ingrese un número natural: "))
                if self.numeroNatural < 0 :
                    raise NumeroNegativoException
                break
            except ValueError as err:
                print("Ingrese un número natural.  Intente otra vez...")
            except NumeroNegativoException as err:
                print("Ingrese un número entero y positivo.  Intente otra vez...")
        return self.numeroNatural

    def divisores(self):
        numero = self.numeroNatural
        contador = 0
        for divisor in range(1, numero + 1):
            if (numero % divisor) == 0:
                print(divisor, "es divisor")
                contador += 1
        print("el numero ", numero, " tiene ", contador, " divisores")

def MCD(PrimerNum,SegundoNum):
    while SegundoNum:
        PrimerNum, SegundoNum = SegundoNum, PrimerNum%SegundoNum
    return print(f"El MCD de Los números es : {PrimerNum}")

