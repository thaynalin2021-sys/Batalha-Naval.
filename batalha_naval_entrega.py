# Jogo: Batalha Naval
# Autora: Thayna Nalin
# Data: Novembro/2025
# Descrição: Implementação simples do jogo Batalha Naval em Python para entrega acadêmica.

import random

def criar_tabuleiro(tamanho):
    return [["~"] * tamanho for _ in range(tamanho)]

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))
    print()

def posicionar_navios(tabuleiro, quantidade):
    tamanho = len(tabuleiro)
    navios = []
    while len(navios) < quantidade:
        x = random.randint(0, tamanho - 1)
        y = random.randint(0, tamanho - 1)
        if (x, y) not in navios:
            navios.append((x, y))
    return navios

def jogar():
    tamanho = 5
    tentativas = 10
    quantidade_navios = 3

    tabuleiro = criar_tabuleiro(tamanho)
    navios = posicionar_navios(tabuleiro, quantidade_navios)

    print("🌊 BEM-VINDO AO JOGO BATALHA NAVAL 🌊")
    print("Você tem", tentativas, "tentativas para encontrar", quantidade_navios, "navios!\n")

    while tentativas > 0:
        imprimir_tabuleiro(tabuleiro)
        try:
            linha = int(input("Escolha a linha (0 a 4): "))
            coluna = int(input("Escolha a coluna (0 a 4): "))
        except ValueError:
            print("Digite apenas números válidos!\n")
            continue

        if linha < 0 or linha >= tamanho or coluna < 0 or coluna >= tamanho:
            print("Coordenadas fora do tabuleiro!\n")
            continue

        if tabuleiro[linha][coluna] != "~":
            print("Você já tentou essa posição!\n")
            continue

        if (linha, coluna) in navios:
            print("🎯 Acertou um navio!\n")
            tabuleiro[linha][coluna] = "X"
            navios.remove((linha, coluna))
            if not navios:
                print("🏆 Parabéns! Você afundou todos os navios!")
                break
        else:
            print("🌊 Errou! Nenhum navio nessa posição.\n")
            tabuleiro[linha][coluna] = "O"
            tentativas -= 1

    if navios:
        print("\n💥 Suas tentativas acabaram!")
        print("Os navios estavam nas posições:", navios)

    print("\nBoa sorte com a entrega! 🚀")

if __name__ == "__main__":
    jogar()
