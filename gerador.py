import random


quantidade = 6


def aleatorio(fim):
	num = []
	for i in range(1000):
		inicio = random.randrange(fim, fim+38)
		fim = random.randrange(inicio+5, inicio+100)
		num.append(random.randrange(inicio, fim))
	return [embaralhar(num), fim]

def embaralhar(numeros):
	final = ["", "", "", "", ""]
	for i in numeros:
		indice = random.randrange(0, 5)
		final[indice] += str(i) + "\n"
	return "".join(final)


for j in range(quantidade):
	nome = 'numeros/numeros_' + str(j+1) + '.txt'
	arquivo = open(nome, 'w+')
	fim = 0
	for i in range(10 ** j):
		resultado = aleatorio(fim)
		fim = resultado[1]
		arquivo.write(resultado[0])
	arquivo.close()	
