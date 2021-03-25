import galois
import mymath
import numpy as np
#import main
import itertools


"""
GF = galois.GF2m_factory(4)
polinomio = galois.Poly([1, 0], field=GF)
resultado = polinomio(1)
print(int(resultado))
"""


#print("ola")
"""
Lugi ten estos sets [[1, 214, 215], [97, 170, 203], [2, 177, 179]] e perdeu o valor correspondiente o set 203
Esta é a palabra codificada [4,27,28,245,206,105,158,80,152]
Interesanos a parte do set de recuperacion. 
O set é [97, 170, 203]
os valores asociados son [245,206,105] (obviamente o 105 non o sabemos que foi o que se perdeu)
Sabemos que f(97)=245 e sabemos que f(170)=206
Calculando o polinomio de grado 1 que pasa por eses puntos quedanos [66 82]. Evaluamos ese polinomio en 203 e tennos que dar 105

GF = galois.GF2m_factory(8)
polinomio = galois.Poly([66, 82], field=GF)
print(polinomio)
print(int(polinomio(97)))
print(int(polinomio(170)))
print(int(polinomio(203)))
"""



from sage.all import *

#points = [(a**6+a**5+1,a**7+a**6+a**5+a**4+a**2+1), (a**7+a**5+a**3+a,a**7+a**6+a**3+a**2+a)]

field = GF(2**8, 'a')
a = field.gen()
R = PolynomialRing(field, "x")
points = [(a**6+a**5+1,a**7+a**6+a**5+a**4+a**2+1), (a**7+a**5+a**3+a,a**7+a**6+a**3+a**2+a)]
polynom = R.lagrange_polynomial(points)
print(polynom.coefficients(sparse=False))
print(polynom(a**7+a**6+a**3+a+1))


"""
def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)
        print(num % 2) 

def binaryToDecimal(binary):
    field = GF(2**8, 'a')
    a = field.gen()
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * a ** i
        binary = binary//10
        i += 1
    print(decimal)  
"""


print(bin(256)[2:])