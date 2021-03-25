#!/home/lionel/Universidade/Segunto_cuatri/sage/sage-9.2/sage -python3
import os
import glob
import json
from sage.all import *

class lrc():
    def __init__(self):
        if os.path.isfile("conf.json"):
            data = json.load(open("conf.json"))
            self.N = data["N"]
            self.K = data["K"]
            self.R = data["R"]
            self.Q = data["Q"]
            self.RSets = data["RSets"]
        else:
            self.N = 9
            self.K = 4
            self.R = 2
            self.Q = 8
            self.RSets = [[1, 214, 215], [97, 170, 203], [2, 177, 179]]
        self.read_files()

    def read_files(self):
        fileList = sorted(glob.glob('TestFile.shar*'))
        self.files_data = []
        for data_file in fileList:
            f = open(data_file, "rb")
            string_data = f.read().decode("utf-8")
            ascii_data = [ord(x) for x in string_data]
            self.files_data.append(ascii_data)
            f.close()
        

    def getWord(self, byte_position):
        word = [x[byte_position] for x in self.files_data ]            
        return word

decoder = lrc()

for i in range(0,4):
    print(decoder.getWord(i))



"""


decoder = lrc()
for i in range(0,4):
    data = [chr(x) for x in decoder.read_byte_posticion(i) ]
    print(data)
"""


"""
field = GF(2**8, 'a')
a = field.gen()
R = PolynomialRing(field, "x")
points = [(a**6+a**5+1,a**7+a**6+a**5+a**4+a**2+1), (a**7+a**5+a**3+a,a**7+a**6+a**3+a**2+a)]
polynom = R.lagrange_polynomial(points)
print(polynom.coefficients(sparse=False))
print(polynom(a**7+a**6+a**3+a+1))

"""

"""
Lugi ten estos sets [[1, 214, 215], [97, 170, 203], [2, 177, 179]] e perdeu o valor correspondiente o set 203
Esta é a palabra codificada [4,27,28,245,206,105,158,80,152]
Interesanos a parte do set de recuperacion. 
O set é [97, 170, 203]
os valores asociados son [245,206,105] (obviamente o 105 non o sabemos que foi o que se perdeu)
Sabemos que f(97)=245 e sabemos que f(170)=206
Calculando o polinomio de grado 1 que pasa por eses puntos quedanos [66 82]. Evaluamos ese polinomio en 203 e tennos que dar 105
"""
"""
https://stackoverflow.com/questions/48065360/interpolate-polynomial-over-a-finite-field
"""


