#Os valores inseridos pelo usuário podem ser números decimais.
from math import *

#Funções de calculo
def AreaRetangulo(x,y):
	area = x*y
	return area

def Hipotenusa(z,w):
	somacatetos = (z**2+w**2)
	hipo = sqrt(somacatetos)
	return hipo

#terminal
def main():
	print("1. Area do Retangulo")
	print("2. Hipotenusa do triangulo retagulo")
	opcao = int(input("Escolha uma opcao:"))
	a = float(input("Forneca o primeiro valor:"))
	b = float(input("Forneca o segundo valor:"))
	if opcao == 1:
		print(AreaRetangulo(a,b))
	elif opcao == 2:
		print(Hipotenusa(a,b))
	else:
		print("opcao invalida")
	
if __name__ == "__main__":
    main()