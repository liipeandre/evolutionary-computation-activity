from bitarray import bitarray
from random import randrange
from random import random

class Individuo(object): 
    def __init__(self, tam_cromossomo):
        # Cria o individuo com o cromossomo e o lugar para o resultado da funcao fitness.
        
        self.resultado_funcao_fitness = 0
        self.quantia_dinheiro = 0.0

        self.cromossomo = bitarray()
        
        # E preencho o cromossomo aleatóriamente com zero's e um's.
        i = 0
        while i < tam_cromossomo:
            bit = randrange(0, 2)
            self.cromossomo.append(True if bit == 1 else False)
            i += 1
            
    def Decodificacao(self):

        # 3 - Decodificacao do cromossomo do individuo.
        
        # Decodificando o total de moedas de 1 real (máximo de 20, porque a quantia maior é 20,00).

        moedas_1_real = self.cromossomo[0] * pow(2, 4)
        moedas_1_real += self.cromossomo[1] * pow(2, 3)
        moedas_1_real += self.cromossomo[2] * pow(2, 2)
        moedas_1_real += self.cromossomo[3] * pow(2, 1)
        moedas_1_real += self.cromossomo[4] * pow(2, 0)        


        # Decodificando o total de moedas de 50 centavos.
        
        moedas_50_cent = self.cromossomo[5] * pow(2, 0)

        # Decodificando o total de moedas de 25 centavos.        

        moedas_25_cent = self.cromossomo[6] * pow(2, 0)  
        
        # Decodificando o total de moedas de 10 centavos.

        moedas_10_cent = self.cromossomo[7] * pow(2, 1)
        moedas_10_cent += self.cromossomo[8] * pow(2, 0)   
        
        # Decodificando o total de moedas de 5 centavos.
        
        moedas_5_cent = self.cromossomo[9] * pow(2, 0)

        # Decodificando o total de moedas de 1 centavo.

        moedas_1_cent = self.cromossomo[10] * pow(2, 2)  
        moedas_1_cent += self.cromossomo[11] * pow(2, 1) 
        moedas_1_cent += self.cromossomo[12] * pow(2, 0) 
        
        # Calculo a quantia em reais que representa este cromossomo.
 
        self.quantia_dinheiro = (moedas_1_real * 1.00) + (moedas_50_cent * 0.50) + (moedas_25_cent * 0.25) + (moedas_10_cent * 0.10) + (moedas_5_cent * 0.05) + (moedas_1_cent * 0.01)
        self.quantia_dinheiro = round(self.quantia_dinheiro, 2)        

        # e retorno a quantidade de cada moeda
        return [moedas_1_real, moedas_50_cent, moedas_25_cent, moedas_10_cent, moedas_5_cent, moedas_1_cent]


    def Funcao_Fitness(self, moedas_1_real, moedas_50_cent, moedas_25_cent, moedas_10_cent, moedas_5_cent, moedas_1_cent):
        
        # 2 - Definicao da funcao fitness 

        # Se o cromossomo for invalido, aplico uma punicao no fitness (nesse caso, 1000 é a punicao).        
        # Se o cromossomo for valido, calculo o fitness e armazeno o resultado no individuo.

        if moedas_10_cent > 2 or moedas_1_cent > 4 or moedas_1_real > 20:
            self.resultado_funcao_fitness = 1000        
        else:
            self.resultado_funcao_fitness = moedas_1_real + moedas_50_cent + moedas_25_cent + moedas_10_cent + moedas_5_cent + moedas_1_cent    
            



    def Mutacao(self, taxa_mutacao):
        # Se a taxa de mutacao for maior que o resultado randomico...
        if taxa_mutacao > randrange(0,100):
            
            # Escolho um bit do cromossomo do individuo...
            posicao_randomica = randrange(0, len(self.cromossomo)-1)
            
            # E inverto o bit (se for 0(false) vira 1(true) e vice-versa.
            self.cromossomo[posicao_randomica] = True if self.cromossomo[posicao_randomica] == False else True




    def Imprima(self):
        print("Individuo: " + str(self.cromossomo))
        print("Fitness: " + str(self.resultado_funcao_fitness) + "\n")