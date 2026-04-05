from Individuo import Individuo
from Populacao import Populacao
from os import system

# 1 - Crio a Populacao Inicial

tam_populacao = 500
tam_cromossomo = 3

populacao = Populacao(tam_populacao, tam_cromossomo)

geracao_atual = 1

while True:
    
    while len(populacao.individuos) <= populacao.tam_populacao: 
        
        # 3 - Decodifico o cromossomo e aplico a funcao de fitness.

        for i in range(0, len(populacao.individuos)):
                      
            # decodificacao do cromossomo
            cromossomo_decodificado = populacao.individuos[i].Decodificacao()
            
            # calculo da funcao fitness
            populacao.individuos[i].Funcao_Fitness(cromossomo_decodificado[0], cromossomo_decodificado[1], cromossomo_decodificado[2])


        # 4 - Selecao por 1 dos metodos abaixo
        
        #pai1 = populacao.Selecao_Randomica()
        #pai2 = populacao.Selecao_Randomica()

        pai1 = populacao.Selecao_Roleta()
        pai2 = populacao.Selecao_Roleta()

        #pai1 = populacao.Selecao_Torneio()
        #pai2 = populacao.Selecao_Torneio()




        # 5 - Crossover por 1 dos metodos abaixo e Mutacao (dentro do crossover)
        
        taxa_mutacao = 0.05        

        populacao.Crossover_Flat(pai1, pai2, taxa_mutacao)





    # Imprime a Geracao Atual em Tela.

    print("\n")
    print("Geracao " + str(geracao_atual)+ "\n")
    populacao.Imprima()
    print("\n\n\n\n")


    

    # 6 - Selecao da Geracao Seguinte

    #populacao.Selecao_Proxima_Geracao_Elitismo()
    
    porcentagem_melhores = 60
    porcentagem_piores = 20

    populacao.Selecao_Proxima_Geracao_Porcentagem(porcentagem_melhores, porcentagem_piores)  





    # 7 - Criterio de Parada

    if populacao.individuos[0].resultado_funcao_fitness < 0.001:
        break;
    geracao_atual += 1
