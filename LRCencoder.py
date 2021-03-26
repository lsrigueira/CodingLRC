import mymath
import numpy as np
import encoder
import galois
import json
import timeit

class lrc(encoder.Encoder) :

    def __init__(self, n=9, k=4, r=2, q=4):
        self.N = n
        self.K = k
        self.R = r
        self.P = 2
        self.M = 4
        self.Q = 2** q
        self.chunksize = k
        self.GF = galois.GF2m_factory(q)
        self.g_x = self.generate_gx() #This method also create a "self.RSet" variable with the sets you need (not all of them)
        self.write_file_configuration()

    def write_file_configuration(self):
        configuration = {
            "N":self.N,
            "K":self.K,
            "R":self.R,
            "P":self.P,
            "M":self.M,
            "Q":self.Q,
            "RSets":self.Rsets
        }
        y = json.dumps(configuration)
        f = open("conf.json","w")
        f.write(y)
        f.close()


    def __str__(self):
        return "LRC encoder. Parameters{N:"+str(self.N)+" K:"+str(self.K)+" R:"+str(self.R) \
            + " P:"+str(self.P) + " M:"+str(self.M) +" Q:"+str(self.Q) +" GF:"+str(self.GF)

    def encode(self, k_symbols_data):
        encoded_data = []
        encoded_data.append(self.encode_chunk(k_symbols_data))
        return encoded_data

    def encode_chunk(self, information):
        while len(information) != self.chunksize:
            information.append("0")
        information = np.array(information)
        bit_matrix = mymath.from_array_to_matrix(information, self.R, (self.K//self.R))
        evaluation_vector = self.create_evaluation_vector(bit_matrix)
        coded_info = []
        for i in range(0,len(self.Rsets)):
            for j in range (0, self.R+1):
                coded_info.append(evaluation_vector(self.Rsets[i][j]))
        coded_info = [ int(x) for x in coded_info ]
        coded_info = [ chr(x) for x in coded_info ]
        return coded_info

    def generate_gx(self):
        g_x = 0
        for i in range(0,pow(2,self.R)): #Numero de polinomio de orden r+1
            g_x = self.next_polynomial(g_x)
            if not self.exist_in_galois_field(g_x):
                continue
            else:
                if self.cumple_conficiones(g_x):
                    return g_x
                continue
        return g_x

    def next_polynomial(self, g_x):
        if g_x == 0:
            new_g_x = [1]
            for i in range(0,self.R+1):#Grado del polinomio es r+1
                new_g_x.append(0)
            return new_g_x
        else:
            g_x = mymath.suma_binaria(bin(int(''.join(map(str, g_x)), 2) << 1),1)
            mymath.from_binary_to_coefs(g_x)

        return [1,0,0,0]

    def cumple_conficiones(self, g_x):
        """
            We need n/(r+1) subsets of points of Fq. Each subset should have r+1 elements
        """
        #print("PASA POR AQUI")
        matriz_evaluacion = self.get_evaluation_matrix(g_x)
        all_sets = self.get_sets(matriz_evaluacion)
        #print(all_sets)
        if len(all_sets) >= self.N / (self.R+1):
            self.Rsets = []
            for i in range (0, self.N // (self.R+1)):
                self.Rsets.append(all_sets[i])
            return True
        
        return False

    def get_evaluation_matrix(self, g_x):
        """
            Evaluate g_x in each point of Fq. The number evaluated will be placed in the result row \n
            i.e-> if g(x)=x^3 in F_{13} and we are evaluating 5. We will put the 5 into the matrix_evaluation row 8 (as 5^3 mod 13 = 8)
        """
        evaluation_matrix = [[] for x in range(self.Q)]
        for i in range (self.Q): #Se valoran todos los numeros de Fq
            galois_polinomial= galois.Poly(g_x, field=self.GF)
            evaluation_matrix[galois_polinomial(i)].append(i)
        return evaluation_matrix

    def get_sets(self, matrix):
        Rset = []
        for i in range(len(matrix)):
            #print(len(matrix[i]))
            if len(matrix[i]) >= self.R +1:
                new_set = [matrix[i][j] for j in range(self.R+1)]
                Rset.append(new_set)
        return Rset

    def exist_in_galois_field(self, polinomio):
        return True

    def create_evaluation_vector(self, bit_matrix):
        x_polinomial = galois.Poly([1], field=self.GF)
        x = galois.Poly([1, 0], field=self.GF)
        f_x_coef = []
        for i in range(0, self.R): # We have R rows
            second_sumatory_coeficients = self.get_second_summatory(i, bit_matrix)
            coeficient_i = x_polinomial * second_sumatory_coeficients
            f_x_coef.append(coeficient_i)
            #print(str(x_polinomial) +" * "+ str(second_sumatory_coeficients) +" = "+ str(coeficient_i))
            x_polinomial = x_polinomial * x #This is intruction is equivalent to multiply the polinomial by the independent variable (usually x)
        f_x = mymath.sum_elemts_galois_array(self.GF, f_x_coef)
        #print("VECTOR FINAL:" + str(f_x))
        return f_x

    def get_second_summatory(self, fila, bit_matrix):
        coeficients = []
        g_x = galois.Poly(self.g_x, field=self.GF)
        for j in range(0, self.K//self.R): # we have k//r columns
            matrix_element = galois.Poly([int(bit_matrix[fila,j])], self.GF)
            #print("g(X)= "+str(g_x) +"-----j= "+str(j))
            g_x_upto_j = g_x ** j
            newcoef = matrix_element * g_x_upto_j
            #print( "g(X)^j= " +str(g_x_upto_j) +"-----matrix_element= "+str(matrix_element)+ "-----Result:"+str(newcoef) )
            coeficients.append(newcoef) 
        polinomio_final = galois.Poly([0],self.GF)
        for i in range(0, mymath.len_galois_array(coeficients)):
            polinomio_final = polinomio_final + coeficients[i]
        
        return polinomio_final