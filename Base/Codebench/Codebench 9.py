def Mdc(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def main():
    resultados = []

    while True:
        a = int(input())
        b = int(input())
        if a == 0 or b == 0:
            break
        resultados.append(Mdc(a, b))
        
    for res in resultados:print(res)

if __name__ == "__main__":
    main()