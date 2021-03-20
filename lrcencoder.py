"""
Que pasa se o castear o inputFile non temos un numero de bits múltiplo de "k"?
"""

"""
Contantes de momento para probar o arquivo
"""
import constant

def get_information_from_files():
    print("Files information stores")
    f = open("TESTFILE", "r")
    information = f.read()
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
    information = information + information
    return information

def generate_files(encode_data):
    print("THIS IS AVALIABLE ONLY FOR LEN(ENCODED_DATA)=1")
    data_one_chunk = encode_data[0]
    for i in range(0,len(data_one_chunk)):
        f = open("TestFile.shar"+str(i), "w")
        f.write(data_one_chunk[i])
        f.close()

information = get_information_from_files()
k_bits_data = prepareInformation(information)
encode_data = encode(k_bits_data)
print("codedData -->"+ str(encode_data))
generate_files(encode_data)
#answer = decode()
#print(answer)