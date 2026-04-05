from Individuo import Individuo
from Populacao import Populacao

# 1 - Crio a Populaçao Inicial

tam_populacao = 5000

tam_cromossomo = 10

populacao = Populacao(tam_populacao, tam_cromossomo)

geracao_atual = 1

while True:
    
    while len(populacao.individuos) <= populacao.tam_populacao: 
        
        # 3 - Decodifico o cromossomo e aplico a funcao de fitness.
        
        for i in range(0, len(populacao.individuos)):
            cromossomo_decodificado = populacao.individuos[i].Decodificacao()
            populacao.individuos[i].Funcao_Fitness(cromossomo_decodificado[0], cromossomo_decodificado[1])





        # 4 - Selecao por 1 dos métodos abaixo
        
        #pai1 = populacao.Selecao_Randomica()
        #pai2 = populacao.Selecao_Randomica()

        pai1 = populacao.Selecao_Roleta()
        pai2 = populacao.Selecao_Roleta()

        #pai1 = populacao.Selecao_Torneio()
        #pai2 = populacao.Selecao_Torneio()



        taxa_mutacao = 0.25

        # 5 - Crossover e Mutacao

        #populacao.Crossover_1_Ponto(pai1, pai2, taxa_mutacao)
        populacao.Crossover_2_Pontos(pai1, pai2, taxa_mutacao)
        #populacao.Crossover_Uniforme(pai1, pai2, taxa_mutacao)




    # Imprime a Geracao Atual em Tela.

    print("\n")
    print("Geracao " + str(geracao_atual)+ "\n")
    populacao.Imprima()
    print("\n\n\n\n")





    # 6 - Selecao da Geracao Seguinte
    
    porcentagem_melhores = 60
    porcentagem_piores = 20

    #populacao.Selecao_Proxima_Geracao_Elitismo()
    populacao.Selecao_Proxima_Geracao_Porcentagem(porcentagem_melhores, porcentagem_piores) 






    # 7 - Criterio de Parada

    if  populacao.individuos[0].resultado_funcao_fitness == 0:
        break
    geracao_atual += 1