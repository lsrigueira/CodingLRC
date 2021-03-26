#!/home/lionel/Universidade/Segunto_cuatri/sage/sage-9.2/sage -python3
import os
import glob
import json
import math
import mymath
import decoder
from sage.all import *

def new_decodification():
    if os.path.isfile("Decodified.txt"):
        os.remove("Decodified.txt")
class lrc(decoder.Decoder):
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
            self.Q = 256
            self.RSets = [[1, 214, 215], [97, 170, 203], [2, 177, 179]]
        try:
            self.words_dict = json.load(open("words_dict.json"))
        except FileExistsError:
            print("No dictionary to tranlate")
            exit()
        self.read_files()

    def read_file(self, i):
        f = open('TestFile.shar'+str(i), "rb")
        string_data = f.read().decode("utf-8")
        ascii_data = [ord(x) for x in string_data]
        f.close()
        return ascii_data

    def read_files(self):
        self.files_data = []
        i=1
        while (i <= self.N):
            try:
                file_data = self.read_file(i)
                self.files_data.append(file_data)
                i=i+1
            except FileNotFoundError:
                try:
                    files_to_complete_set = ((self.R+1) - (i % (self.R+1))) % (self.R+1)
                    self.files_data.append("MISSING")
                    incremento = 1
                    for j in range(1, files_to_complete_set+1):
                        incremento = incremento +1
                        file_data = self.read_file(i+j)    
                        self.files_data.append(file_data)   
                    self.recover_file(i)
                    self.files_data[i-1] = self.read_file(i)
                    i = i + incremento
                except FileNotFoundError:
                    print("More than one fail in the same set. Cant recover")
                """
                1--> falla o primeiro --> leer dous mais 
                2--> falla o segundo --> leer un mais
                0--> falla o ultimo  --> non leer
                """

    def recover_file(self, file_num):
        #print("Vamos a recuperar o arquivo "+str(file_num))
        field = GF(self.Q, 'a')
        a = field.gen()
        R = PolynomialRing(field, "x")
        x_points, pointo_to_recover = self.get_x_point_to_recover_file(file_num)
        #? This points are got using RSets, they are independent from the lenght of the original file
        #Changuing format
        try:
            for word in range(0,100):
                y_points = self.get_y_points_to_recover_file(file_num, word)
                points_to_evaluate = []
                for i in range(0, len(x_points)):
                    points_to_evaluate.append((x_points[i],y_points[i]))
                polynom = R.lagrange_polynomial(points_to_evaluate)
                recovery_point_sage = polynom(pointo_to_recover)
                #print("**********************************")
                recovered_data = int(str(super().from_polinomial_sage_to_decimal(recovery_point_sage)))
                #print(recovered_data)
                #print("**********************************")
                self.write_file_symbol(file_num,chr(recovered_data))
        except IndexError:
            print("File recovered")
    
    def get_y_points_to_recover_file(self, file_num, word):
        set_number = self.get_sets_index_belong_file(file_num)
        y_points = []
        
        for i in range(1, (self.R+1)+1 ): #Index begin in one (so we have R+1)
            if not (i + ((self.R+1) * set_number) == file_num):
                #print(self.files_data[(i + (self.R+1) * set_number) -1])
                data = self.files_data[ (i + (self.R+1) * set_number) -1][word] #FIles start in 1. Files_data is a local list (start at 0)
                #print("Recuperar-->" +str(file_num)+"  LENDO-->" +str(i + (self.R+1) * set_number)+ " PALABRA--->" +str(word)+ " Data-->"+ str(data))
                y_points.append(super().from_decimal_to_sage_polinomial(data))
        return y_points


    def get_sets_index_belong_file(self, file_num):
        """
            Range from 0 to N-1
        """
        set_number = math.floor(float(file_num-1)/float(len(self.RSets)))
        return set_number


    def get_RSets_from_file(self, file_num):
        get_sets_index =  self.get_sets_index_belong_file(file_num)
        return self.RSets[get_sets_index]

    def get_x_point_to_recover_file(self, file_num):
        specific_set = self.get_RSets_from_file(file_num)
        index_point_inside_set = (file_num -1 ) % (self.R+1)
        specific_set_sega_version = []
        point_to_recover = 0
        for i in range(0,len(specific_set)):
            if(i == index_point_inside_set ):
                point_to_recover = super().from_decimal_to_sage_polinomial(specific_set[i])
            else:
                specific_set_sega_version.append(super().from_decimal_to_sage_polinomial(specific_set[i]))
        return specific_set_sega_version, point_to_recover    
        #return "a","b"

    def write_file_symbol(self, file_num, symbol):
        f = open("TestFile.shar"+str(file_num), "ab")
        f.write(symbol.encode('utf-8'))
        f.close()


    def getWord(self, byte_position):
        word = []
        for i in range(0,len(self.files_data)):
            word.append(self.files_data[i][byte_position])
        return word

    def translate(self, word):
        return self.words_dict[str(word)]

new_decodification()
decoder = lrc()
print(decoder.words_dict)
i=-1
while True:
    i=i+1
    try:
        coded_word = decoder.getWord(i)
        print(coded_word)
        decoded_word = [chr(x) for x in decoder.translate(coded_word)]
        f = open("Decodified.txt", "ab")
        for j in range(0,len(decoded_word)):
            f.write(decoded_word[j].encode('utf-8'))
        f.close()

    except IndexError:
        print("End of decodification")
        exit()