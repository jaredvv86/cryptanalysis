from GematriaPrimus import rune_to_prime
from LiberPrimus import page40

def product(ls):
	prod=1
	for i in ls:
		prod*=i
	return prod



prime40=[rune_to_prime(char) for char in page40]


for i in range(3,len(prime40)+1):
	group=prime40[i-3:i]
	print(product(group))

print(prime40[-3::])

if __name__ == "__main__":
	main()