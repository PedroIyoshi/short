import sys

sys.setrecursionlimit(10_000)
def quick(num):
	if len(num) == 1:
		return num
	elif len(num) != 0:
		comparador = num[len(num)-1]
		num = num[0:len(num) - 1]
		if len(num) == 1:
			if num[0] <= comparador:
				return num + [comparador]
			return [comparador] + num
		maior = []
		menor = []
		for i in num:
			if i > comparador:
				maior.append(i)
			else:
				menor.append(i)
		menor = quick(menor) if menor != None else []
		maior = quick(maior) if maior != None else []

		menor = menor if menor != None else []
		maior = maior if maior != None else []
		return menor + [comparador] + maior 