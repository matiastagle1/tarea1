def primo(numero):
    if numero < 2:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True

numero = int(input("Ingresa un número: "))

if primo(numero):
    print("Primo")
else:
    print("No es primo")








