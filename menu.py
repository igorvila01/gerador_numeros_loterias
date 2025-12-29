import random

def gerador_numeros_mega(qtd): 
    qtd = len(jogos_ms)+qtd   
    while len(jogos_ms) < qtd:
        aposta = sorted(random.sample(range(1,61),6)) 
        if aposta not in jogos_ms.values():
            jogo = f'{len(jogos_ms)+1}'
            jogos_ms[jogo] = aposta

def gerador_numeros_lotofacil(qtd):
    qtd = len(jogos_lf)+qtd
    while len(jogos_lf) < qtd:
        aposta = sorted(random.sample(range(1,26),15))
        jogo = f'{len(jogos_lf)+1}'
        jogos_lf[jogo] = aposta



def lista_jogos(jogos):
    for chave, numeros in jogos.items():
        print(chave, numeros)

    

menu = """
== Digite o numero da aposta desejada ==        
1 - Mega Sena
2 - Loto Facil
3 - Quina
4 - Sair
"""

jogos_ms = {}
jogos_lf = {}


while True:
    try:
        menu_selecionado = int(input(menu))

    except ValueError:
        print('Menu Selecionado Inválido! Tente novamente!')
        continue

    match menu_selecionado:
        case 1: 
            while True:
                try:
                    qtd_jogos = int(input('Digite a quantidade de jogos que quer gerar:'))
                    print()
                    break
                except ValueError:
                    print('Quantidade Invalida! Digite novamente!')
                    continue            
            
            gerador_numeros_mega(qtd_jogos)
            lista_jogos(jogos_ms)
        
        case 2:
            ...
        
        case 3:
            ...

        case 4:
            break
        
        case _:
            print('Entrada Invalida! Escolha opção correta!')
            continue
            


    