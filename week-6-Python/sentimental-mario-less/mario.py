# TODO
altura = 0

while True:
    try:
        altura = int(input("Enter altura: "))

        if altura >= 1 and altura <= 8:
            break
        else:
            print("Height must be between 1 and 8 inclusive.")
    except ValueError:
        print("Invalid input. Height must be a numeric value.")

for linha in range(altura):
    for espaco in range(altura - linha - 1):
        print(" ", end="")

    for colunas in range(linha + 1):
        print("#", end="")

    print()
