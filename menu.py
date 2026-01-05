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
            return qtd_jogos
            
        except ValueError:
            print('Quantidade Invalida! Digite novamente!')
            continue        

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
jogos_quina = {}

while True:
    try:
        menu_selecionado = int(input(menu))

    except ValueError:
        print('Menu Selecionado Inválido! Tente novamente!')
        continue

    match menu_selecionado:
        case 1:             
            quantidade = solicita_quantidade()                         
            gerador_jogos(jogos_ms, quantidade, 60, 6)
            lista_jogos(jogos_ms)
        
        case 2:
            quantidade = solicita_quantidade()
            gerador_jogos(jogos_lf, quantidade, 25, 15)
            lista_jogos(jogos_lf)
        
        case 3:
            quantidade = solicita_quantidade()
            gerador_jogos(jogos_quina, quantidade, 80, 5)
            lista_jogos(jogos_quina)

        case 4:
            break
        
        case _:
            print('Entrada Invalida! Escolha opção correta!')
            continue
            