import numpy as np


# Testa se é o numero é 1, 2 ou 3.
def testa_posicao(numero2):
    teste = False
    while teste != True:
        if numero2 == 1:
            teste = True
        elif numero2 == 2:
            teste = True
        elif numero2 == 3:
            teste = True
        else:
            print('Posição invalida')
            numero2 = int(input('Digite posição valida: '))
    return numero2


# Testa se é letra ou numero.
def testa_se_numero(numero1):
    while numero1.isdigit() == False:
        if numero1.isdigit() == True:
            pass
        else:
            print('A posição tem que ser um número')
            numero1 = input('Digite número valido: ')
    return int(numero1)


# testa se uma casa já foi ocupada.
def testa_casa_ocupada(linha, coluna, vez, jogada):
    verificador4 = False
    while verificador4 == False:
        if tabuleiro[linha, coluna] == 'X':
            print('Casa ocupada')
            linha = input(f"{vez} digite a posição na horizontal: ")
            linha = testa_se_numero(linha)
            linha = testa_posicao(linha)
            coluna = input(f"{vez} digite a posição na vertical: ")
            coluna = testa_se_numero(coluna)
            coluna = testa_posicao(coluna)
        elif tabuleiro[linha, coluna] == 'O':
            print('Casa ocupada')
            linha = input(f"{vez} digite a posição na horizontal: ")
            linha = testa_se_numero(linha)
            linha = testa_posicao(linha)
            coluna = input(f"{vez} digite a posição na vertical: ")
            coluna = testa_se_numero(coluna)
            coluna = testa_posicao(coluna)
        else:
            tabuleiro[linha, coluna] = jogada
            verificador4 = True


tabuleiro = np.array([[' ', '_', '_', '_'], [' ', '_', '_', '_'], [' ', '_', '_', '_'], [' ', ' ', ' ', ' ']])

jogador1 = input('Digite nome do jogador 1: ')
jogador2 = input('Digite nome do jogador 2: ')

print(f'{jogador1}: x        {jogador2}:O')
print(f'    1   2   3')
print(f' 1 _{tabuleiro[1,1]}_|_{tabuleiro[1,2]}_|_{tabuleiro[1,3]}_')
print(f' 2 _{tabuleiro[2,1]}_|_{tabuleiro[2,2]}_|_{tabuleiro[2,3]}_')
print(f' 3  {tabuleiro[3,1]} | {tabuleiro[3,2]} | {tabuleiro[3,3]} ')


xouo = 'a'
verificador = 'b'
verificador2 = 1
linha = 0
coluna = 0
contador = 1

while verificador != xouo:
    verificador3 = verificador2 % 2
    if verificador3 == 0:
        vez = jogador2
    else:
        vez = jogador1
    verificador2 = verificador2 + 1

    if vez == jogador1:
        jogada = "X"
    else:
        jogada = "O"

    linha = input(f"{vez} digite a posição na horizontal: ")
    linha = testa_se_numero(linha)
    linha = testa_posicao(linha)
    coluna = input(f"{vez} digite a posição na vertical: ")
    coluna = testa_se_numero(coluna)
    coluna = testa_posicao(coluna)

    testa_casa_ocupada(linha, coluna, vez, jogada)

    xouo = jogada
    xouo = xouo + xouo + xouo

    print(f'{jogador1}: x        {jogador2}:O')
    print(f'    1   2   3')
    print(f' 1 _{tabuleiro[1, 1]}_|_{tabuleiro[1, 2]}_|_{tabuleiro[1, 3]}_')
    print(f' 2 _{tabuleiro[2, 1]}_|_{tabuleiro[2, 2]}_|_{tabuleiro[2, 3]}_')
    print(f' 3  {tabuleiro[3, 1]} | {tabuleiro[3, 2]} | {tabuleiro[3, 3]} ')

    win1 = tabuleiro[1, 1] + tabuleiro[1, 2] + tabuleiro[1, 3]
    win2 = tabuleiro[2, 1] + tabuleiro[2, 2] + tabuleiro[2, 3]
    win3 = tabuleiro[3, 1] + tabuleiro[3, 2] + tabuleiro[3, 3]
    win4 = tabuleiro[1, 1] + tabuleiro[2, 1] + tabuleiro[3, 1]
    win5 = tabuleiro[1, 2] + tabuleiro[2, 2] + tabuleiro[3, 2]
    win6 = tabuleiro[1, 3] + tabuleiro[2, 3] + tabuleiro[3, 3]
    win7 = tabuleiro[1, 1] + tabuleiro[2, 2] + tabuleiro[3, 3]
    win8 = tabuleiro[1, 3] + tabuleiro[2, 2] + tabuleiro[3, 1]

    if win1 == xouo:
        verificador = xouo
    elif win2 == xouo:
        verificador = xouo
    elif win3 == xouo:
        verificador = xouo
    elif win4 == xouo:
        verificador = xouo
    elif win5 == xouo:
        verificador = xouo
    elif win6 == xouo:
        verificador = xouo
    elif win7 == xouo:
        verificador = xouo
    elif win8 == xouo:
        verificador = xouo
    elif contador == 9:
        xouo = 'velha'
        verificador = xouo

    contador = contador + 1

if xouo == 'XXX':
    print(f"{jogador1} é o campeão")
elif xouo == 'OOO':
    print(f"{jogador2} é o campeão")
else:
    print('Deu velha')

print(f'{jogador1}: x        {jogador2}:O')
print(f'    1   2   3')
print(f' 1 _{tabuleiro[1,1]}_|_{tabuleiro[1,2]}_|_{tabuleiro[1,3]}_')
print(f' 2 _{tabuleiro[2,1]}_|_{tabuleiro[2,2]}_|_{tabuleiro[2,3]}_')
print(f' 3  {tabuleiro[3,1]} | {tabuleiro[3,2]} | {tabuleiro[3,3]} ')
