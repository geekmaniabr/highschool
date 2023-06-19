from random import seed, random
# Fazendo todas as definições separadamente antes de começar o gerador
# Definindo a função que nos gera as amostras
def GeradordeAmostras(a, b, n):
    # Aplicando o número USP como uma semente
    NUSP = 14783977
    seed(NUSP)
    # Criando as n amostras que o usuário deseja
    amostra = n * [0]
    for k in range(n):
        #fazemos valores "aleatórios" e que respeitem os limites inferiores e superiores
        amostra[k] = a + (b - a)*random()
    return amostra

# Criando os intervalos de classe
def GeradordeIntervalos(a, b, m):
    # Criamos um lista vazia
    intervalos_de_classe = []
    # Definimos o tamanho de cada intervalo
    intervalo_tamanho = (b - a) / m
    # Garantimos que cada intervalo não irá exceder o tamanho máximo permitido
    limite_inferior = a
    limite_superior = a + intervalo_tamanho

    for k in range(m):
        # Inserimos os intervalos por meio de listas dentro da lista de intervalos de classe
        intervalos_de_classe.append([limite_inferior, limite_superior])
        # Após o limite inferior ser usado, ele passa a ter o tamanho do superior
        limite_inferior = limite_superior
        # Um novo valor ao limite superior é atribuído
        limite_superior += intervalo_tamanho

    return intervalos_de_classe

def GeradordeFrequencias(amostra, intervalos_de_classe):
    # Inicializa uma lista de frequências com zeros e de mesmo tamanho da lista de intervalos de classe
    frequencias = [0] * len(intervalos_de_classe)

    # Atribuiremos para a variável amostra_atual os valores de cada elemento da lista amostra
    for amostra_atual in amostra:
        # A comparação irá percorrer cada valor do limite superior do intervalo de classe
        for j in range(len(intervalos_de_classe)):
            # A comparação em sequência verifica se cada valor da amostra atual é menor que o limite superior
            # Caso valor nao seja, a sua frequencia permanece zero e é verificado se pertence ao próximo intervalo
            if amostra_atual >= intervalos_de_classe[j][0] and amostra_atual < intervalos_de_classe[j][1]:
                frequencias[j] += 1
                break

    return frequencias

def histograma(intervalos, frequencias):
    print("Gráfico")

    # Imprime as barras do histograma
    n = len(intervalos)
    h = max(frequencias)
    for i in range(h-1, -1, -1):
        linha = ""
        # Caso a frequencia seja maior ou igual o valor atual a barra é impressa, caso contrário ela fica em branco
        for freq in frequencias:
            if i < freq:
                linha += "%5s " % ("\u2593")
            else:
                linha += " "*5 + " "
        print(linha)

    # Imprime os limites inferiores dos intervalos
    limites_inf = ""
    for intervalo in intervalos:
        limites_inf += "%5.2f " % intervalo[0]
    print(limites_inf)

    # Imprime os limites superiores dos intervalos
    limites_sup = ""
    for intervalo in intervalos:
        limites_sup += "%5.2f " % intervalo[1]
    print(limites_sup)

    # Imprime as frequências
    freqs = ""
    for freq in frequencias:
        freqs += "%5.03d " % freq
    print(freqs)

def informacoes():
    # Solicita ao usuário os limites e informações para gerar o histograma
    print("Limites [a, b) com a < b e a >= 0")
    a = float(input("Entre com a (seu limite inferior): "))

    # Verifica se o limite inferior é válido (positivo)
    if a >= 0:
        b = float(input("Entre com b (seu limite superior): "))

        # Verifica se o limite superior é válido (maior que o inferior)
        if b > a:
            n = int(input("Qual o tamanho da sua amostra?: "))

            # Gera a amostra com base nos limites e no tamanho informados
            amostra = GeradordeAmostras(a, b, n)
            print("Amostra:")
            #formata para 2 casas decimais todos os valores na lista em amostra
            print(" ".join("{:.2f}".format(i) for i in amostra))
            print()

            totaldeintervalos = int(input("Qual será o Número de Intervalos?: "))

            # Verifica se o número de intervalos é válido (intervalos não muito pequenos)
            if (b - a) / totaldeintervalos >= 0.01:

                # Gera os intervalos de classe com base nos limites e no número de intervalos informados
                intervalos = GeradordeIntervalos(a, b, totaldeintervalos)

                # Gera as frequências para cada intervalo com base na amostra gerada
                frequencias = GeradordeFrequencias(amostra, intervalos)

                # Imprime os intervalos e suas frequências
                print("%s %12s" % ("Intervalo", "Frequencia"))
                for i, intervalo in enumerate(intervalos):
                    print("%.2f ATÉ %.2f%10.03d" % (intervalo[0], intervalo[1], frequencias[i]))
                print()

                # Gera o histograma com base nos intervalos e frequências gerados
                histograma(intervalos, frequencias)

            else:
                print("Há intervalos demais, por favor, insira os dados novamente")
                gerahistograma()
        else:
            print("Seu limite superior é menor que o inferior, por favor, insira os dados novamente.")
            gerahistograma()
    else:
        print("O limite inferior precisa ser positivo, por favor, insira os dados novamente.")
        gerahistograma()

def gerahistograma():
    while True:
        print()  # linha em branco
        informacoes()
        autorizacao = input("Quer fazer outro histograma? sim/não: ")
        if autorizacao.lower() not in ["sim", "s"]:
            print("fim do programa")
            break

gerahistograma()

