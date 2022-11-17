def verificador(path):
	arquivo = open(path, "r").read().split('\n')
	numeros = list(
		map(
			lambda i:int(i), arquivo
		)
	)

	organizado = True
	for i in range(1, len(numeros), 2):
		if numeros[i] < numeros[i-1]:
			organizado = False
			print(numeros[i-1], numeros[i])
			break
	if organizado:
		print("Os numeros estão organizados")
	else:
		print("Os numeros estão desorganizados")
