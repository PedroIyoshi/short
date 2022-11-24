def insertion(n)
    for i in 1...(n.length)
        valor = n[i]
        temp = i
        while temp > 0 && n[temp - 1] > valor
            n[temp] = n[temp - 1]
            temp = temp - 1
        end
        n[temp] = valor
    end
    return n
end