from jogo import jogar


def main():
    """
    Função principal do programa.
    Controla o loop geral do jogo, permitindo
    que o jogador jogue novamente se desejar.
    """
    while True:
        # Inicia uma partida do jogo
        jogar()

        # Pergunta ao jogador se deseja jogar novamente
        if input("Deseja jogar novamente? (s/n): ").lower() != "s":
            print("Obrigado por jogar! Até a próxima")
            break


if __name__ == "__main__":
    main()
