def insertion(n):
    for i in range( 1, len( n ) ):
        chave = n[i]
        j = i
        while j > 0 and chave < n[j - 1]:
            n[j] = n[j - 1]
            j -= 1
        n[j] = chave
    return n
