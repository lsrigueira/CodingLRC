import numpy as np
import galois
from galois_field.GF import GF, FFElement
from galois_field.fast_polynom import FastPolynom

class galoisField:

    """    
    def __init__(self, p, exp, irr_poly={0: 1, 1: 1, 4: 1}):
        irr_poly = FastPolynom(irr_poly)
        self.gfield = GF(2, m=4, irr=irr_poly)
        self.polinomials = []
        for i in range(0,constant.Q):
            self.polinomials.append(FFElement(self.gfield,FastPolynom({i:1})))
        

    def show_polinomials(self):
        for i in range(0,len(self.polinomials)):
            print(self.polinomials[i])
    """     

def from_string_to_binary(information):
    print("Casting to binary-->"+information)
    binary_information = information
    #binary_information = ''.join(format(ord(i), '08b') for i in information) 
    return binary_information

def from_bitstring_to_matrix(information, rows, columns):
    np_bit_array = from_bitstring_to_np_array(information)
    matrix = np_bit_array.reshape(rows, columns)
    return matrix

def from_bitstring_to_np_array(information):
    np_bit_array = np.array(information[0])
    for i in range(1,len(information)):
        np_bit_array = np.append(np_bit_array,information[i])
    return np_bit_array

def from_binary_to_coefs(binario):
    coefs = []
    for i in range (0,len(binario)):
        coefs.append(int(binario[i:i+1]))
    return coefs


def split_information_into_k_chunks(k, binary_information):
    """
        Split binary_information into k chunks
    """
    print("Splitting the information into chunks of size "+ str(k))
    splitted_information = []
    try:
        for i in range(0,len(binary_information),4):
            splitted_information.append(binary_information[i:i+4])
    except:
        print("NON SE INTRODUCIU UN NUMERO MULTIPLO DE K")
    return splitted_information

def suma_binaria(num1,num2):
    sum = bin(int(num1, 2) + int(num2, 2))
    return sum[2:] 

def polinomial_sum(arraypolinomios):
    polinomio_final = 0
    for i in range(0, len(arraypolinomios)):
        polinomio_final = np.polyadd(polinomio_final, arraypolinomios[i])
    return polinomio_final


def polinomial_power(polinomio, exponente):
    """
        Polinoial up to exponent
    """
    static_polinomio = polinomio
    if exponente == 0:
        return [1]
    for j in range(0,exponente-1):
        polinomio = np.polymul(polinomio,static_polinomio)
    return polinomio