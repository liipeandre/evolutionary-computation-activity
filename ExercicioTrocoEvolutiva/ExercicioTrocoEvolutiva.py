from Individuo import Individuo
from Populacao import Populacao
from os import system

# Leio o valor que o usuario quer calcular

quantia_dinheiro = float(input("Digite a Quantia Recebida: \n"))

# 1 - Crio a Populacao Inicial

tam_populacao = 500
tam_cromossomo = 6

populacao = Populacao(tam_populacao, tam_cromossomo)

geracao_atual = 1

# declaro a variavel que receber� o resultado.

melhor_individuo = Individuo(tam_cromossomo)

while True:
    
    while len(populacao.individuos) <= populacao.tam_populacao: 
        
        # 3 - Decodifico o cromossomo e aplico a funcao de fitness.

        for i in range(0, len(populacao.individuos)):
                      
            # decodificacao do cromossomo
            cromossomo_decodificado = populacao.individuos[i].Decodificacao()
            
            # calculo da funcao fitness
            populacao.individuos[i].Funcao_Fitness(cromossomo_decodificado[0], cromossomo_decodificado[1], cromossomo_decodificado[2], cromossomo_decodificado[3], cromossomo_decodificado[4], cromossomo_decodificado[5])

        # verifico se a quantia lida � igual a de algum cromossomo, se nao for, esse cromossomo ser� penalizado.

        for i in range(0, len(populacao.individuos)):
            if quantia_dinheiro != populacao.individuos[i].quantia_dinheiro:
                populacao.individuos[i].resultado_funcao_fitness += 10


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

    condicao_parada = False
    for i in range(0, len(populacao.individuos)):
        if quantia_dinheiro == populacao.individuos[0].quantia_dinheiro and populacao.individuos[0].resultado_funcao_fitness < 10:
            condicao_parada = True
            
            

    if condicao_parada == True: 
        melhor_individuo = populacao.individuos[0]
        break
    geracao_atual += 1


# Imprimo o melhor individuo, que � o resultado

system("cls")

print("Melhor Individuo: " + str(melhor_individuo.cromossomo) + "\n")
print("Fitness: " + str(melhor_individuo.resultado_funcao_fitness) + "\n")
print("Quantia Lida: " + str(quantia_dinheiro) + "\n")
print("Quantia Cromossomo: " + str(melhor_individuo.quantia_dinheiro) + "\n")

cromossomo_decodificado = melhor_individuo.Decodificacao()

print("Moedas de 1 Real: " + str(cromossomo_decodificado[0]) + "\n") 
print("Moedas de 50 Centavos: " + str(cromossomo_decodificado[1]) + "\n")
print("Moedas de 25 Centavos: " + str(cromossomo_decodificado[2]) + "\n")
print("Moedas de 10 Centavos: " + str(cromossomo_decodificado[3]) + "\n")
print("Moedas de 5 Centavos: " + str(cromossomo_decodificado[4]) + "\n")
print("Moedas de 1 Centavo: " + str(cromossomo_decodificado[5]) + "\n")

