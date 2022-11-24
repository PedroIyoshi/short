def quick(num)
	return num if num.size == 1
	return [] if num.size == 0

	comparador = num.pop
	if(num.size == 1)
		a = num.size
		return [num[0], comparador] if num[0] < comparador
		return [comparador, num[0]]
	end
	maior = []
	menor = []

	for i in 0..num.size - 1  do
		if(num[i] > comparador)
			maior.push(num[i])
		else
			menor.push(num[i])
		end
	end
	menor = quick(menor)
	maior = quick(maior)
	menor.push(comparador)
	return menor.concat(maior)
end
