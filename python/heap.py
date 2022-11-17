# n = getn()
n = [3, 4, 15, 0, 1, 8, 41, 163, 84, 1384, 2, 0.5, 98]
n = [1, 2, 3] 

def swap(i, a):
	s = n[i]
	n[i] = n[i * 2 + a]
	n[i * 2 + a] = s
	return True

def heap():
	while True: 
		for i in range(len(n)-1):
			if i * 2 + 1 >= len(n):
				break
			elif i * 2 + 2 >= len(n):
				f1 = n[i * 2 + 1]
				if n[i] < f1:	
					a = 1
				break
			else:
				f1 = n[i * 2 + 1]
				f2 = n[i * 2 + 2]
			if n[i] < f1 and n[i] < f2:
				if f1 > f2: a = 1
				else: a = 2
			elif n[i] < f1: a = 1
			elif n[i] < f2: a = 2
			trava = False if a == 0 else swap(i, a)
		if not trava: 
			break
	print(n)
heap()