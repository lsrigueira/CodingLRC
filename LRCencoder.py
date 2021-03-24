import mymath
import numpy as np
import encoder
import galois

class lrc(encoder.Encoder) :

    def __init__(self, n=9, k=4, r=2):
        self.N = n
        self.K = k
        self.R = r
        self.P = 2
        self.M = 4
        self.Q = 16
        self.GF = galois.GF2m_factory(4)

    def __str__(self):
        return "LRC encoder. Parameters{N:"+str(self.N)+" K:"+str(self.K)+" R:"+str(self.R) \
            + " P:"+str(self.P) + " M:"+str(self.M) +" Q:"+str(self.Q) +" GF:"+str(self.GF)

    def encode(self, k_bits_data):
        print("Encoding Information")
        encoded_data = []
        for i in range(0,len(k_bits_data)):
            encoded_data.append(self.encode_chunk(k_bits_data[i]))
        return encoded_data

    def encode_chunk(self, information):
        print("Encoding chunk, we are replicating now")
        bit_matrix = mymath.from_bitstring_to_matrix(information, self.R, self.K//self.R)
        evaluation_vector = self.create_evaluation_vector(bit_matrix)
        Rsets = [[1, 3, 9], [2, 5, 6], [4, 10 ,12]]
        for i in range(0,len(Rsets)):
            for j in range (0,3):
                print(evaluation_vector(Rsets[i][j]))
        print(evaluation_vector)
        information = information + information
        return information

    def generate_gx(self):
        g_x = 0
        for i in range(0,pow(2,self.R)): #Numero de polinomio de orden r+1
            g_x = self.next_polynomial(g_x)
            print("ola")
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
        matriz_evaluacion = self.get_evaluation_matrix(g_x)
        all_sets = self.get_sets(matriz_evaluacion)
        print(matriz_evaluacion)
        print(all_sets)
        print("end")
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
        print(g_x)
        evaluation_matrix = [[] for x in range(self.Q)]
        for i in range (self.Q): #Se valoran todos los numeros de Fq
            galois_polinomial= galois.Poly(g_x, field=self.GF)
            evaluation_matrix[galois_polinomial(i)].append(i)
        return evaluation_matrix

    def get_sets(self, matrix):
        Rset = []
        for i in range(len(matrix)):
            if len(matrix[i]) >= self.R +1:
                new_set = [matrix[i][j] for j in range(self.R+1)]
                Rset.append(new_set)
        return Rset

    def exist_in_galois_field(self, polinomio):
        return True

    def create_evaluation_vector(self, bit_matrix):
        x_polinomial = [1]
        f_x_coef = []
        g_x = self.generate_gx()
        for i in range(0, self.R): # We have R rows
            second_sumatory_coeficients = self.get_second_summatory(i, bit_matrix, g_x)
            coeficient_i = np.polymul(x_polinomial,second_sumatory_coeficients)
            f_x_coef.append(coeficient_i)
            #print(str(x_polinomial) +" * "+ str(second_sumatory_coeficients) +" = "+ str(coeficient_i))
            x_polinomial.append(0) #This is intruction is equivalent to multiply the polinomial by the independent variable (usually x)
        f_x = mymath.polinomial_sum(f_x_coef)
        galois_f_x = galois.Poly(f_x, field=self.GF)
        return galois_f_x

    def get_second_summatory(self, fila, bit_matrix, g_x):
        coeficients = []
        g_x = galois.Poly(g_x,field=self.GF)
        for j in range(0, self.K//self.R): # we have k//r columns
            matrix_element = galois.Poly([int(bit_matrix[fila,j])], self.GF)
            #print("g(X)= "+str(g_x) +"-----j= "+str(j))
            g_x_upto_j = g_x ** j
            newcoef = matrix_element * g_x_upto_j
            #print( "g(X)^j= " +str(g_x_upto_j) +"-----matrix_element= "+str(matrix_element)+ "-----Result:"+str(newcoef) )
            coeficients.append(newcoef) 
        print("eeee")
        polinomio_final = galois.Poly([0],self.GF)
        for i in range(0, mymath.len_galois_array(coeficients)):
            polinomio_final = polinomio_final + coeficients[i]
        
        #DE MOMENTO ASI
        #finalform = mymath.polinomial_sum(coeficients)
        #print("Second Sumatory-----"+str(finalform))
        return polinomio_final