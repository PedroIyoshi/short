def bubble(n):
	while True:
		pronto = True
		for i in range(len(n)):
			if i == 0: 
				continue
			if(n[i-1] > n[i]):
				pronto = False
				temp = n[i]
				n[i] = n[i - 1]
				n[i - 1] = temp
		if pronto:
			break
	return n
