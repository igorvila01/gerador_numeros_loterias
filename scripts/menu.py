import textwrap

def mostrar_menu():   
    menu = textwrap.dedent("""\
    == Digite o numero da aposta desejada ==        
    1 - Mega Sena
    2 - Loto Facil
    3 - Quina
    4 - Sair
    """)

    return menu