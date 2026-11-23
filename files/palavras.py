from pathlib import Path

# Pasta onde estão os arquivos de palavras (mesma pasta deste arquivo)
PASTA = Path(__file__).parent


def carregar_palavras(nome_arquivo):
    """
    Lê um arquivo de palavras (uma por linha) e devolve
    um set com todas as palavras em minúsculo.
    """
    with open(PASTA / nome_arquivo, "r", encoding="utf-8") as arquivo:
        return {linha.strip().lower() for linha in arquivo if linha.strip()}


# Todas as palavras aceitas como palpite (lista do repositório do Gabriel)
# É um set porque a busca é muito mais rápida que em lista
PALAVRAS_VALIDAS = carregar_palavras("palavras_validas.txt")

# Palavras do dia a dia, usadas só para sortear a palavra secreta
PALAVRAS = sorted(carregar_palavras("palavras_comuns.txt"))

# Configurações do jogo
TAMANHO = 5
TENTATIVAS = 6
