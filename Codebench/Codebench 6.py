def Verificar(n):
    if n > 0:
        return "positivo"
    elif n < 0:
        return "negativo"
    else:
        return "valor nulo"

def main():
    numero = int(input())
    resultado = Verificar(numero)
    print(resultado)

if __name__ == "__main__":
    main()