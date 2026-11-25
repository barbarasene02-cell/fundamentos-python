
import random

opcoes = ["pedra", "papel", "tesoura"]

pontos_jogador = 0
pontos_computador = 0

print("=== JOGO DE JOKENPÔ ===")

while True:

    jogador = input(
        "\nEscolha pedra, papel ou tesoura: "
    ).lower().strip()

    if jogador not in opcoes:
        print("Opção inválida! Tente novamente.")
        continue

    computador = random.choice(opcoes)

    print("Você escolheu:", jogador)
    print("Computador escolheu:", computador)

    if jogador == computador:
        print("Empate!")

    elif (
        (jogador == "pedra" and computador == "tesoura")
        or (jogador == "papel" and computador == "pedra")
        or (jogador == "tesoura" and computador == "papel")
    ):
        print("Você ganhou!")
        pontos_jogador += 1

    else:
        print("O computador ganhou!")
        pontos_computador += 1

    print("\n=== PLACAR ===")
    print("Você:", pontos_jogador)
    print("Computador:", pontos_computador)

    continuar = input(
        "\nDeseja continuar? (s/n): "
    ).lower().strip()

    if continuar == "n":
        print("\nFim de jogo!")
        break

    elif continuar != "s":
        print("Resposta inválida! Encerrando o jogo.")
        break
