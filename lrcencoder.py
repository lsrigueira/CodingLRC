"""
Que pasa se o castear o inputFile non temos un numero de bits múltiplo de "k"?
Temos que facer 16 ou 256?
Todos os polinomios de grado r+1 pertenecen a F(x)

"""

"""
Contantes de momento para probar o arquivo
"""
import constant
import mymath
import numpy as np
from numpy.polynomial import polynomial as P

def get_information_from_files():
    print("Files information stores")
    f = open("TESTFILE", "r")
    information = f.read().strip()
    return information

def prepareInformation(information):
    binary_information = mymath.from_string_to_binary(information)
    splitted_information = mymath.split_information_into_k_chunks(constant.K, binary_information)
    return splitted_information

def encode(k_bits_data):
    print("Encoding Information")
    encoded_data = []
    for i in range(0,len(k_bits_data)):
        encoded_data.append(encode_chunk(k_bits_data[i]))
    return encoded_data

def encode_chunk(information):
    print("Encoding chunk, we are replicating now")
    bit_matrix = mymath.from_bitstring_to_matrix(information)
    evaluation_vector = create_evaluation_vector(bit_matrix)
    print(evaluation_vector)
    information = information + information
    return information

def generate_files(encode_data):
    print("THIS IS AVALIABLE ONLY FOR LEN(ENCODED_DATA)=1")
    data_one_chunk = encode_data[0]
    for i in range(0,len(data_one_chunk)):
        f = open("TestFile.shar"+str(i), "w")
        f.write(data_one_chunk[i])
        f.close()

def generate_gx():
    g_x = 0
    for i in range(0,pow(2,constant.R)): #Numero de polinomio de orden r+1
        g_x = next_polynomial(g_x)
        if not exist_in_galois_field(g_x):
            continue
        else:
            if cumple_conficiones(g_x):
                return g_x
            continue
    return g_x

def next_polynomial(g_x):
    if g_x == 0:
        new_g_x = [1]
        for i in range(0,constant.R+1):#Grado del polinomio es r+1
            new_g_x.append(0)
        return new_g_x
    else:
        g_x = mymath.suma_binaria(bin(int(''.join(map(str, g_x)), 2) << 1),1)
        mymath.from_binary_to_coefs(g_x)

    return [1,0,0,0]

def cumple_conficiones(g_x):
    return True

def exist_in_galois_field(polinomio):
    return True

def create_evaluation_vector(bit_matrix):
    x_polinomial = [1]
    f_x_coef = []
    g_x = generate_gx()
    for i in range(0,constant.FILAS):
        second_sumatory_coeficients = get_second_summatory(i, bit_matrix, g_x)
        coeficient_i = np.polymul(x_polinomial,second_sumatory_coeficients)
        f_x_coef.append(coeficient_i)
        #print(str(x_polinomial) +" * "+ str(second_sumatory_coeficients) +" = "+ str(coeficient_i))
        x_polinomial.append(0) #This is intruction is equivalent to multiply the polinomial by the independent variable (usually x)
    f_x = mymath.polinomial_sum(f_x_coef)
    return f_x

def get_second_summatory(fila, bit_matrix, g_x):
    coeficients = []
    for j in range(0, constant.COLUMNAS):
        matrix_element = [int(bit_matrix[fila,j])]
        #print("g(X)= "+str(g_x) +"-----j= "+str(j))
        g_x_upto_j = mymath.polinomial_power(g_x,j)
        newcoef = np.polymul(matrix_element,g_x_upto_j)
        #print( "g(X)^j= " +str(g_x_upto_j) +"-----matrix_element= "+str(matrix_element)+ "-----Result:"+str(newcoef) )
        coeficients.append(newcoef) 
    finalform = mymath.polinomial_sum(coeficients)
    #print("Second Sumatory-----"+str(finalform))
    return finalform

information = get_information_from_files()
k_bits_data = prepareInformation(information)
encode_data = encode(k_bits_data)
#print("codedData -->"+ str(encode_data))
generate_files(encode_data)
#answer = decode()
#print(answer)