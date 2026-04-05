from bitarray import bitarray
from random import randrange
from random import random

class Individuo(object): 
    def __init__(self, tam_cromossomo):
        # Cria o individuo com o cromossomo e o lugar para o resultado da funcao fitness.
        
        self.resultado_funcao_fitness = 0

        self.cromossomo = bitarray()
        
        # E preencho o cromossomo aleatóriamente com zero's e um's.
        i = 0
        while i < tam_cromossomo:
            bit = randrange(0, 2)
            self.cromossomo.append(True if bit == 1 else False)
            i += 1
            
    def Decodificacao(self):

        # 3 - Decodificacao do cromossomo do individuo.

        i = 0
        soma = 0
        produto = 1
        while i < len(self.cromossomo):
            if self.cromossomo[i] == False:
                soma += (i + 1)
            else:
                produto *= (i + 1)
            i += 1
        
        return [soma, produto]


    def Funcao_Fitness(self, soma, produto):
        
        # 2 - Definicao da funcao fitness 

        # Se o cromossomo for invalido, aplico uma punicao no fitness (nesse caso, não existe).

        # Se o cromossomo for valido, calculo o fitness       
        
        # e no final, armazeno o resultado no individuo.

        self.resultado_funcao_fitness = abs(36 - soma + 360 - produto )    




    def Mutacao(self, taxa_mutacao):
        # Se a taxa de mutacao for maior que o resultado randomico...
        if taxa_mutacao > randrange(0, 100):
            
            # Escolho um bit do cromossomo do individuo...
            posicao_randomica = randrange(0, len(self.cromossomo)-1)
            
            # E inverto o bit (se for 0(false) vira 1(true) e vice-versa.
            self.cromossomo[posicao_randomica] = True if self.cromossomo[posicao_randomica] == False else True




    def Imprima(self):
        print("Individuo: " + str(self.cromossomo))
        print("Fitness: " + str(self.resultado_funcao_fitness) + "\n")