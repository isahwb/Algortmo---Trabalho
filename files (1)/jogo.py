import random

from palavras import PALAVRAS, TENTATIVAS
from utils import (pedir_palpite, calcular_cores, mostrar_tabuleiro,
                   quadrado, VERDE, AMARELO, CINZA)


def escolher_palavra():
    """
    Escolhe aleatoriamente a palavra secreta da lista de palavras.
    """
    return random.choice(PALAVRAS)


def jogar():
    """
    Função principal do jogo.
    Controla o fluxo da partida, tentativas e mensagens ao jogador.
    """
    nome = input("Digite seu nome para iniciar o jogo: ")

    # Exibe as regras do jogo
    print(f"""
    Bem-vindo(a), {nome}!
        - A palavra secreta tem 5 letras
        - Você tem {TENTATIVAS} tentativas
        - {quadrado("A", VERDE)} letra certa no lugar certo
        - {quadrado("A", AMARELO)} letra existe na palavra, mas em outro lugar
        - {quadrado("A", CINZA)} letra não existe na palavra
""")

    palavra_secreta = escolher_palavra()
    historico = []  # guarda (palpite, cores) de cada tentativa

    for tentativa in range(1, TENTATIVAS + 1):
        palpite = pedir_palpite()
        cores = calcular_cores(palpite, palavra_secreta)
        historico.append((palpite, cores))

        mostrar_tabuleiro(historico)

        # Verifica se o jogador acertou (todas as letras verdes)
        if all(cor == VERDE for cor in cores):
            print(f"Parabéns, {nome}! Você acertou a palavra '{palavra_secreta}' "
                  f"em {tentativa} tentativa(s)!")
            return

        print(f"Tentativas restantes: {TENTATIVAS - tentativa}\n")

    # Caso o jogador não acerte dentro do limite
    print(f"Você perdeu! A palavra era '{palavra_secreta}'.")
