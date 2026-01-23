import random

def gerador_numeros(limitador_jogo, qtd_numeros_jogos):
    return sorted(random.sample(range(1,limitador_jogo+1), qtd_numeros_jogos))   

def gerador_jogos(modalidade, qtd, limite, qtd_min):
    qtd = len(modalidade)+qtd   
    while len(modalidade) < qtd:
        aposta = gerador_numeros(limite, qtd_min)

        if aposta not in modalidade.values():
            jogo = f'{len(modalidade)+1}'
            modalidade[jogo] = aposta

    print('Jogos Realizado com sucesso!')

def solicita_quantidade():
    while True:
        try:
            qtd_jogos = int(input('Digite a quantidade de jogos que quer gerar:'))
            if qtd_jogos <= 0:
                print('Quantidade Invalida! Digite novamente!')
                continue
            return qtd_jogos
            
        except ValueError:
            print('Quantidade Invalida! Digite novamente!')
            continue        

def lista_jogos(jogos):
    for chave, numeros in jogos.items():
        print(chave, numeros)   