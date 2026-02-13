def perfeito (x):
	divisores = 0
	for i in range(1,x):
		if x % i == 0:
			divisores += i
	return divisores == x

def main():
	num = int(input())
	print(perfeito(num))

if __name__ == "__main__":
    main()