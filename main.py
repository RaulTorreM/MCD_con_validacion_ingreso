import Logica.NumeroNatural
from Logica.NumeroNatural import NumeroNatural

if __name__ == '__main__':
    PrimerNum = NumeroNatural()
    SegundNum = NumeroNatural()
    PrimerNumInt =PrimerNum.validarTipo()
    SegundNumInt =SegundNum.validarTipo()
    MCD = Logica.NumeroNatural.MCD(PrimerNumInt,SegundNumInt)
