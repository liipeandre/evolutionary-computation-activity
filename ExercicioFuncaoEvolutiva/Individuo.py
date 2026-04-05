from bitarray import bitarray
from random import randrange
from random import random
from random import uniform
from math import sin

class Individuo(object): 
    def __init__(self, tam_cromossomo):
        # Cria o individuo com o cromossomo e o lugar para o resultado da funcao fitness.
        
        self.resultado_funcao_fitness = 0

        self.cromossomo = []
        
        # E preencho o cromossomo aleatóriamente com valores aleatorios
        
        i = 0
        while i < tam_cromossomo:
            self.cromossomo.append(uniform(-1.0, 1.0))  
            i += 1


    def Decodificacao(self):
        return [self.cromossomo[0], self.cromossomo[1], self.cromossomo[2]]


    def Funcao_Fitness(self, x, y, z): 
        
        # 2 - Definicao da funcao fitness 

        # Se o cromossomo for invalido, aplico uma punicao no fitness (nesse caso, 1000 é a punicao).        
        # Se o cromossomo for valido, calculo o fitness e armazeno o resultado no individuo.

        self.resultado_funcao_fitness = 10 * pow(x - pow(y, 2), 2) + 2 * sin(x) - z * pow(2.711828, -z) + pow(y, 2) * sin(y) 
        self.resultado_funcao_fitness = abs(self.resultado_funcao_fitness)



    def Mutacao(self, taxa_mutacao):
        # Se a taxa de mutacao for maior que o resultado randomico...
        if taxa_mutacao > randrange(0,100):     
            while True:             
                # Escolho um valor do cromossomo do individuo...
            
                posicao1 = randrange(0, len(self.cromossomo)-1)
                posicao2 = randrange(0, len(self.cromossomo)-1)
            
                if posicao1 != posicao2:          
                    # E troco eles de lugar
                    aux = self.cromossomo[posicao1]
                    self.cromossomo[posicao1] = self.cromossomo[posicao2]
                    self.cromossomo[posicao2] = aux
                    break




    def Imprima(self):
        print("Individuo: " + str(self.cromossomo))
        print("Fitness: " + str(self.resultado_funcao_fitness) + "\n")