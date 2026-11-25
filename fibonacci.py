
print("=== SEQUÊNCIA DE FIBONACCI ===")

try:
    quantidade = int(input("Quantos termos deseja ver? "))

    if quantidade <= 0:
        print("Digite uma quantidade maior que zero.")

    else:
        a = 0
        b = 1

        sequencia = []

        for i in range(quantidade):
            sequencia.append(a)

            a, b = b, a + b

        print("Sequência de Fibonacci:")
        print(sequencia)

except ValueError:
    print("Entrada inválida! Digite um número inteiro.")
