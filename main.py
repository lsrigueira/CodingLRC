"""
Que pasa se o castear o inputFile non temos un numero de bits múltiplo de "k"?
Temos que facer 16 ou 256?
Todos os polinomios de grado r+1 pertenecen a F(x)

"""

"""
Contantes de momento para probar o arquivo
"""
import mymath
import numpy as np
from numpy.polynomial import polynomial as P
import LRCencoder
import os
import glob
import json

def new_execution():
    fileList = glob.glob('Test*')
    for data_file in fileList:
        os.remove(data_file)


def get_information_from_files(filename):
    print("Files information stores")
    f = open(filename, "r")
    information = f.read()
    return information

def prepareInformation(information, symbol_lenght):
    binary_information = mymath.from_string_to_binary(information)
    splitted_information = mymath.split_information_into_k_chunks(symbol_lenght, binary_information)
    return splitted_information

def write_files(encode_data):
    for i in range(0,len(encode_data)):
        for j in range(0, len(encode_data[i])):    
            f = open("TestFile.shar"+str(j+1), "ab")
            f.write(encode_data[i][j].encode('utf-8'))
            f.close()


new_execution()
information = get_information_from_files("TESTFILE")
print("We are using ascii which is already a byte (256 bits symbol)")
ascii_data = [ord(ascii_info) for ascii_info in information]
my_encoder = LRCencoder.lrc(9, 4, 2, 8)
encoded_data = []
words_dict = {}
for i in range(0,len(ascii_data),4):
    data_coded = my_encoder.encode_chunk(ascii_data[i:i+4])
    coded_in_asccii = [ord(x) for x in data_coded]
    words_dict[str(coded_in_asccii)]=ascii_data[i:i+4]
    encoded_data.append(data_coded)
write_files(encoded_data)
print(words_dict)
json.dump(words_dict, open("words_dict.json",'w'))

#print(encode_data)
#print("codedData -->"+ str(encode_data))
#answer = decode()
#print(answer)