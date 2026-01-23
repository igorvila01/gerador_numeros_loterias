from scripts import gerador_jogos, solicita_quantidade, lista_jogos
from data_loterias import jogos_ms, jogos_lf, jogos_quina

menu = """
== Digite o numero da aposta desejada ==        
1 - Mega Sena
2 - Loto Facil
3 - Quina
4 - Sair
"""

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
            print('Saindo do programa... Boa sorte!')
            break
        
        case _:
            print('Entrada Invalida! Escolha opção correta!')
            continue
            