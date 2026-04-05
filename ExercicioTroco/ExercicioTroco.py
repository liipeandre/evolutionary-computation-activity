from Individuo import Individuo
from Populacao import Populacao
from os import system

# Leio o valor que o usuario quer calcular

quantia_dinheiro = float(input("Digite a Quantia Recebida: \n"))

# 1 - Crio a Populaçao Inicial

tam_populacao = 1000
tam_cromossomo = 13

populacao = Populacao(tam_populacao, tam_cromossomo)

geracao_atual = 1

fitness_anterior = 0
n_vezes_fitness_nao_alterado = 0

while True:
    
    while len(populacao.individuos) <= populacao.tam_populacao: 
        
        # 3 - Decodifico o cromossomo e aplico a funcao de fitness.

        for i in range(0, len(populacao.individuos)):
                      
            # decodificacao do cromossomo
            cromossomo_decodificado = populacao.individuos[i].Decodificacao()
            
            # calculo da funcao fitness
            populacao.individuos[i].Funcao_Fitness(cromossomo_decodificado[0], cromossomo_decodificado[1], cromossomo_decodificado[2], cromossomo_decodificado[3], cromossomo_decodificado[4], cromossomo_decodificado[5])

        # verifico se a quantia lida é igual a de algum cromossomo, se nao for, esse cromossomo será penalizado.

        for i in range(0, len(populacao.individuos)):
            if quantia_dinheiro != populacao.individuos[i].quantia_dinheiro:
                populacao.individuos[i].resultado_funcao_fitness += 1000


        # 4 - Selecao por 1 dos metodos abaixo
        
        #pai1 = populacao.Selecao_Randomica()
        #pai2 = populacao.Selecao_Randomica()

        pai1 = populacao.Selecao_Roleta()
        pai2 = populacao.Selecao_Roleta()

        #pai1 = populacao.Selecao_Torneio()
        #pai2 = populacao.Selecao_Torneio()




        # 5 - Crossover por 1 dos metodos abaixo e Mutacao
        
        taxa_mutacao = 0.25      

        #populacao.Crossover_1_Ponto(pai1, pai2, taxa_mutacao)
        #populacao.Crossover_2_Pontos(pai1, pai2, taxa_mutacao)
        populacao.Crossover_Uniforme(pai1, pai2, taxa_mutacao)





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

    if fitness_anterior == populacao.individuos[0].resultado_funcao_fitness: 
        n_vezes_fitness_nao_alterado += 1 
    if n_vezes_fitness_nao_alterado == 5:
        break
    geracao_atual += 1


# Imprimo o melhor individuo, que é o resultado

system("cls")

cromossomo_decodificado = populacao.individuos[0].Decodificacao()

print("Moedas de 1 Real: " + str(cromossomo_decodificado[0]) + "\n") 
print("Moedas de 50 Centavos: " + str(cromossomo_decodificado[1]) + "\n")
print("Moedas de 25 Centavos: " + str(cromossomo_decodificado[2]) + "\n")
print("Moedas de 10 Centavos: " + str(cromossomo_decodificado[3]) + "\n")
print("Moedas de 5 Centavos: " + str(cromossomo_decodificado[4]) + "\n")
print("Moedas de 1 Centavo: " + str(cromossomo_decodificado[5]) + "\n")

