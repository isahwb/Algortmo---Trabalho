import os
import unicodedata

from palavras import PALAVRAS_VALIDAS, TAMANHO

# Faz o Windows (cmd/PowerShell) entender as cores do terminal
os.system("")

# Resultados possíveis de cada letra
VERDE = "verde"      # letra certa no lugar certo
AMARELO = "amarelo"  # letra existe na palavra, mas em outra posição
CINZA = "cinza"      # letra não existe na palavra

# Códigos de cor do terminal (fundo + cor da letra)
ESTILOS = {
    VERDE: "\033[48;5;34m\033[1;97m",     # fundo verde, letra branca
    AMARELO: "\033[48;5;220m\033[1;30m",  # fundo amarelo, letra preta
    CINZA: "\033[48;5;240m\033[1;97m",    # fundo cinza, letra branca
}
RESET = "\033[0m"


def remover_acentos(texto):
    """
    Tira os acentos do texto (ex.: 'lápis' -> 'lapis'),
    já que as palavras do arquivo não possuem acento.
    """
    normalizado = unicodedata.normalize("NFD", texto)
    return "".join(c for c in normalizado if unicodedata.category(c) != "Mn")


def pedir_palpite():
    """
    Solicita ao jogador um palpite válido.
    Continua pedindo até que o palpite tenha 5 letras
    e exista na lista de palavras válidas.
    """
    while True:
        palpite = remover_acentos(input(f"Digite seu palpite ({TAMANHO} letras): ").strip().lower())

        if len(palpite) != TAMANHO:
            print(f"O palpite deve ter exatamente {TAMANHO} letras.")
        elif palpite not in PALAVRAS_VALIDAS:
            print("Essa palavra não está na lista de palavras válidas.")
        else:
            return palpite


def calcular_cores(palpite, palavra):
    """
    Compara o palpite com a palavra secreta e devolve uma lista
    com o resultado de cada letra (VERDE, AMARELO ou CINZA).

    Funciona em 2 passadas para tratar letras repetidas corretamente.
    """
    cores = [CINZA] * TAMANHO

    # Conta quantas vezes cada letra da palavra secreta ainda está "disponível"
    disponiveis = {}
    for letra in palavra:
        disponiveis[letra] = disponiveis.get(letra, 0) + 1

    # 1 passada: marca os verdes e gasta essas letras
    for i in range(TAMANHO):
        if palpite[i] == palavra[i]:
            cores[i] = VERDE
            disponiveis[palpite[i]] -= 1

    # 2 passada: marca os amarelos (só se ainda sobrou a letra)
    for i in range(TAMANHO):
        if cores[i] == CINZA and disponiveis.get(palpite[i], 0) > 0:
            cores[i] = AMARELO
            disponiveis[palpite[i]] -= 1

    return cores


def quadrado(letra, cor):
    """
    Devolve um quadrado colorido com a letra dentro.
    """
    return f"{ESTILOS[cor]} {letra.upper()} {RESET}"


def mostrar_tabuleiro(historico):
    """
    Mostra todas as tentativas feitas até agora,
    cada uma como uma linha de quadrados coloridos.
    """
    print()
    for palpite, cores in historico:
        print(" ".join(quadrado(letra, cor) for letra, cor in zip(palpite, cores)))
    print()
