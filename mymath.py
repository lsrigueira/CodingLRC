import constant
import numpy as np


def from_string_to_binary(information):
    print("Casting to binary-->"+information)
    binary_information = information
    #binary_information = ''.join(format(ord(i), '08b') for i in information) 
    return binary_information

def from_bitstring_to_matrix(information):
    np_bit_array = from_bitstring_to_np_array(information)
    matrix = np_bit_array.reshape(constant.R,constant.K//constant.R)
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