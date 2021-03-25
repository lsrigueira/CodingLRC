"""
Que pasa se o castear o inputFile non temos un numero de bits múltiplo de "k"?
Temos que facer 16 ou 256?
Todos os polinomios de grado r+1 pertenecen a F(x)

"""

"""
Contantes de momento para probar o arquivo
"""
import mymath
import galois
import numpy as np
from numpy.polynomial import polynomial as P
import LRCencoder
import os
import glob

def new_execution():
    fileList = glob.glob('Test*')
    for data_file in fileList:
        os.remove(data_file)


def get_information_from_files():
    print("Files information stores")
    f = open("TESTFILE", "r")
    information = f.read()
    return information

def prepareInformation(information, symbol_lenght):
    binary_information = mymath.from_string_to_binary(information)
    splitted_information = mymath.split_information_into_k_chunks(symbol_lenght, binary_information)
    return splitted_information

def write_files(encode_data):
    for i in range(0,len(encode_data)):
        f = open("TestFile.shar"+str(i), "ab")
        f.write(encode_data[i].encode('utf-8'))
        print(ord(encode_data[i]))
        f.close()


new_execution()
information = get_information_from_files()
print("We are using ascii which is already a byte (256 bits symbol)")
ascii_data = [ord(ascii_info) for ascii_info in information]
my_encoder = LRCencoder.lrc(9, 4, 2, 8)

for i in range(0,len(ascii_data),4):
    print("SOLO DISPONIBLE PARA K MULTIPLO DE 4 DE MOMENTO")
    encode_data = my_encoder.encode_chunk(ascii_data)

to_print = [ord(x) for x in encode_data]
print(to_print)
print(my_encoder.Rsets)
write_files(encode_data)
write_files(encode_data)
write_files(encode_data)
write_files(encode_data)

#print(encode_data)
#print("codedData -->"+ str(encode_data))
#answer = decode()
#print(answer)