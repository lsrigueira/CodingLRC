"""
Que pasa se o castear o inputFile non temos un numero de bits múltiplo de "k"?
"""

"""
Contantes de momento para probar o arquivo
"""
import constant
import numpy as np
from numpy.polynomial import polynomial as P

def get_information_from_files():
    print("Files information stores")
    f = open("TESTFILE", "r")
    information = f.read().strip()
    return information

def prepareInformation(information):
    binary_information = from_string_to_binary(information)
    splitted_information = split_information_into_k_chunks(constant.K, binary_information)
    return splitted_information

def encode(k_bits_data):
    print("Encoding Information")
    encoded_data = []
    for i in range(0,len(k_bits_data)):
        encoded_data.append(encode_chunk(k_bits_data[i]))
    return encoded_data

def from_string_to_binary(information):
    print("Casting to binary-->"+information)
    binary_information = information
    #binary_information = ''.join(format(ord(i), '08b') for i in information) 
    return binary_information

def split_information_into_k_chunks(k, binary_information):
    print("Splitting the information into chunks of size "+ str(k))
    splitted_information = []
    try:
        for i in range(0,len(binary_information),4):
            splitted_information.append(binary_information[i:i+4])
    except:
        print("NON SE INTRODUCIU UN NUMERO MULTIPLO DE K")
    return splitted_information

def encode_chunk(information):
    print("Encoding chunk, we are replicating now")
    bit_matrix = from_bitstring_to_matrix(information)
    evaluation_vector = create_evaluation_vector(bit_matrix)
    information = information + information
    return information

def generate_files(encode_data):
    print("THIS IS AVALIABLE ONLY FOR LEN(ENCODED_DATA)=1")
    data_one_chunk = encode_data[0]
    for i in range(0,len(data_one_chunk)):
        f = open("TestFile.shar"+str(i), "w")
        f.write(data_one_chunk[i])
        f.close()

def from_bitstring_to_matrix(information):
    np_bit_array = from_bitstring_to_np_array(information)
    matrix = np_bit_array.reshape(constant.R,constant.K//constant.R)
    return matrix

def from_bitstring_to_np_array(information):
    np_bit_array = np.array(information[0])
    for i in range(1,len(information)):
        np_bit_array = np.append(np_bit_array,information[i])
    return np_bit_array

def generate_gx():
    g_x = [1,0,0,0]
    return g_x

def create_evaluation_vector(bit_matrix):
    x_polinomial = [1]
    for i in range(0,constant.FILAS):
        print("DEBUGGING")
        second_sumatory_coeficients = get_second_summatory(i,bit_matrix)
        #totalp = np.polymul(np.array(x_polinomial, dtype=float), np.array(second_sumatory_coeficients, dtype=float))
        print(second_sumatory_coeficients)
        """
        print(str(x_polinomial) + "*" +str(second_sumatory_coeficients))
        print(totalp)
        print("ULTIMO PASO")
        print(str(totalp) + "*" +str(g_x))
        print(final)
        x_polinomial.append(0)
        """
    print("END OF DEBUGGIN")
    exit
    return "o"

def get_second_summatory(fila, bit_matrix):
    coeficients = []
    g_x = generate_gx()

    for j in range(0,constant.COLUMNAS):
        matrix_element = float(bit_matrix[fila,j])
        print("g(X)= "+str(g_x) +"-----j= "+str(j))
        newpow= P.polypow(g_x,j)
        print(newpow)
        newcoef = np.polymul(matrix_element,newpow)
        
        coeficients.insert(0,newcoef)
    return coeficients

information = get_information_from_files()
k_bits_data = prepareInformation(information)
encode_data = encode(k_bits_data)
print("codedData -->"+ str(encode_data))
generate_files(encode_data)
#answer = decode()
#print(answer)