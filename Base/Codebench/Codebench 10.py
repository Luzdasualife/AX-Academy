def primo(n):
    # Retorna 1 se n é primo, 0 caso contrário
    if n <= 1:
        return 0
    if n == 2:
        return 1
    if n % 2 == 0:
        return 0
    for i in range(3, n):
        if n % i == 0:
            return 0
    return 1

def main():
    numeros = []  
    while True:
        num = int(input())
        if num == 0:
            break
        numeros.append(num)


    for n in numeros:
        if primo(n) == 1:
            print(n)

main()