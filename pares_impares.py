
numeros = []
pares = []
impares = []

print("=== PARES E ÍMPARES ===")
print("Digite os números inteiros.")
print("Digite 'fim' para terminar.")

while True:

    entrada = input("Digite um número: ").strip()

    if entrada.lower() == "fim":
        break

    try:
        numero = int(entrada)

        numeros.append(numero)

        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")

print("\nLista completa:", numeros)
print("Números pares:", pares)
print("Números ímpares:", impares)
