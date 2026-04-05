from Individuo import Individuo
from random import randrange
from random import random

class Populacao(object):  
    def __init__(self, tam_populacao, tam_cromossomo):
        
        # Armazeno os dados da populacao (quantidade e o tamanho do cromossomo de cada individuo)
        
        self.tam_populacao = tam_populacao
        self.tam_cromossomo = tam_cromossomo
        
        # Crio uma lista, que armazenará os individuos.

        self.individuos = []
        
        # Crio um individuo e adiciono na lista de individuos.      

        i = 0
        while i < tam_populacao:
            self.individuos.append(Individuo(tam_cromossomo))
            i += 1




    def Selecao_Randomica(self):
                
        # Seleciono o pai randomicamente

        pai = self.individuos[randrange(0, self.tam_populacao - 1)]
        return pai       



    def Selecao_Roleta(self):

        # Primeiro faço a soma dos fitness de todos os indivíduos

        i = 0
        soma_fitness = 0
        while i < len(self.individuos):
            soma_fitness += self.individuos[i].resultado_funcao_fitness
            i += 1
        soma_fitness = abs(soma_fitness)
        
        # Agora sorteio um número entre 0 e o total do fitness.

        resultado_sorteio = randrange(0, soma_fitness - 1)      
        
        # Agora aplico na fórmula abaixo.
        
        pai = Individuo(self.tam_cromossomo)
        
        i = 0
        somatorio_fitness = 0
        while i < len(self.individuos):
            if somatorio_fitness >= resultado_sorteio:
                pai = self.individuos[i]
                break           
            somatorio_fitness += self.individuos[i].resultado_funcao_fitness
            i += 1
        return pai
                

    def Selecao_Torneio(self):
        # Seleciono os 2 pais randomicamente

        pai1 = self.individuos[randrange(0, self.tam_populacao - 1)]
        pai2 = self.individuos[randrange(0, self.tam_populacao - 1)]

        # E simulo um torneio entre eles.

        k = 0.75
        r = random()

        if r < k:
            return pai1 
        else:
            return pai2      




    def Crossover_Flat(self, individuo1, individuo2, taxa_mutacao):
        # para cada gene do cromossomo...
        i = 0
        while i < self.tam_cromossomo - 1: 
            maior = -999999
            menor = 999999
            # testo qual gene dos dois pais é maior (para definir o intervalo).
            if(individuo1.cromossomo[i] > individuo2.cromossomo[i]):
                maior = individuo1.cromossomo[i]
                menor = individuo2.cromossomo[i]
            else:
                maior = individuo2.cromossomo[i]
                menor = individuo1.cromossomo[i]

            # seleciono um valor aleatorio no intervalo e adiciono nos filhos.
            valor_escolhido1 = 0
            valor_escolhido2 = 0
            if menor != maior:
                valor_escolhido1 = randrange(menor, maior)        
                valor_escolhido2 = randrange(menor, maior)             

            filho1 = Individuo(self.tam_cromossomo)    
            filho2 = Individuo(self.tam_cromossomo) 

            filho1.cromossomo.append(valor_escolhido1)
            filho2.cromossomo.append(valor_escolhido2)
            i += 1
        
        # Aplico a mutação nos filhos

        filho1.Mutacao(taxa_mutacao);
        filho2.Mutacao(taxa_mutacao);  

        # Decodifico o cromossomo dos filhos

        cromossomo_decodificado_f1 = filho1.Decodificacao()
        cromossomo_decodificado_f2 = filho2.Decodificacao()        

        # Calculo o fitness dos 2 filhos
        
        filho1.Funcao_Fitness(cromossomo_decodificado_f1[0], cromossomo_decodificado_f1[1], cromossomo_decodificado_f1[2], cromossomo_decodificado_f1[3], cromossomo_decodificado_f1[4], cromossomo_decodificado_f1[5])
        filho2.Funcao_Fitness(cromossomo_decodificado_f2[0], cromossomo_decodificado_f2[1], cromossomo_decodificado_f2[2], cromossomo_decodificado_f2[3], cromossomo_decodificado_f2[4], cromossomo_decodificado_f1[5])       

        # Adiciono os filhos na população
        
        self.individuos.append(filho1)
        self.individuos.append(filho2)




    
    def Selecao_Proxima_Geracao_Elitismo(self):
        
        # Ordeno a minha população, de acordo com o fitness.
        
        # Reverse = False = Ordenacao Ascendente (Menores no Inicio, Problema de Minimizacao).
        # Reverse = True  = Ordenacao Descendente (Menores no Final, Problema de Maximizacao).
             
        self.individuos.sort(key=lambda Individuo: Individuo.resultado_funcao_fitness, reverse=False)
        
        # E excluo os piores que ficaram da posição tam_populacao para frente (pois o crossover faz a população dobrar de tamanho)
        
        del self.individuos[self.tam_populacao:]


    def Selecao_Proxima_Geracao_Porcentagem(self, porcentagem_melhores, porcentagem_piores):
        
        # Ordeno a minha população, de acordo com o fitness.
        
        # Reverse = False = Ordenacao Ascendente (Menores no Inicio, Problema de Minimizacao).
        # Reverse = True  = Ordenacao Descendente (Menores no Final, Problema de Maximizacao).
             
        self.individuos.sort(key=lambda Individuo: Individuo.resultado_funcao_fitness, reverse=False)
        
        # calculo quantos elementos do inicio da lista (melhores) eu vou selecionar para a próxima geracao.
        # o calculo é uma regra de tres simples.        

        num_melhores = int((self.tam_populacao * porcentagem_melhores)/100) 
        
        # calculo quantos elementos do fim da lista (piores) eu vou selecionar para a próxima geracao. 

        num_piores = int((self.tam_populacao * porcentagem_piores)/100)     

        # entao descarto o que não estiverem nesses dois intervalos acima.

        del self.individuos[num_melhores:self.tam_populacao - num_piores]


    def Imprima(self):
        self.individuos.sort(key=lambda Individuo: Individuo.resultado_funcao_fitness, reverse=False)
        self.individuos[0].Imprima()
