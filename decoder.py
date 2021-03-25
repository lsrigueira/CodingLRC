from abc import ABC
from sage.all import *

class Decoder(ABC):
    
    @classmethod
    def encode(self, data):
        ...
    @classmethod
    def __init__(self, n=9, k=4, r=2):
        self.n = n
        self.k = k
        self.r = r
        ...
    
    def from_decimal_to_sage_polinomial(self, decimal):
        return self.from_binary_to_sage_polinomial(int(bin(decimal)[2:]))

    def from_binary_to_sage_polinomial(self, binary):
        field = GF(2**8, 'a')
        a = field.gen()
        binary1 = binary
        poly, i, n = 0, 0, 0
        while(binary != 0):
            dec = binary % 10
            poly = poly + dec * a ** i
            binary = binary//10
            i += 1
        return poly 

    def from_polinomial_sage_to_decimal(self, polynomial):
        print("---------------")
        polynomial_str = str(polynomial).replace("1"," 0").replace(" a "," 1 ").replace("a^","")
        index = [int(x.strip())+1 for x in polynomial_str.split("+")]
        print(polynomial)
        binario = None
        for i in range(1,index[0]+1):
            if i in index:
                binario = "1" if binario is None else "1" + binario 
            else:
                binario = "0" if binario is None else "0" + binario 
        decimal = int(binario, 2)
        return decimal
        #print(str(polynomial).replace)