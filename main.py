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

def get_information_from_files():
    print("Files information stores")
    f = open("TESTFILE", "r")
    information = f.read().strip()
    return information

def prepareInformation(information, symbol_lenght):
    binary_information = mymath.from_string_to_binary(information)
    splitted_information = mymath.split_information_into_k_chunks(symbol_lenght, binary_information)
    return splitted_information

def generate_files(encode_data):
    print("THIS IS AVALIABLE ONLY FOR LEN(ENCODED_DATA)=1")
    data_one_chunk = encode_data[0]
    for i in range(0,len(data_one_chunk)):
        f = open("TestFile.shar"+str(i), "w")
        f.write(data_one_chunk[i])
        f.close()


information = get_information_from_files()
k_bits_data = prepareInformation(information, 4)
my_encoder = LRCencoder.lrc(9,4,2)
print(my_encoder.__str__())
encode_data = my_encoder.encode(k_bits_data)
#print("codedData -->"+ str(encode_data))
generate_files(encode_data)
#answer = decode()
#print(answer)