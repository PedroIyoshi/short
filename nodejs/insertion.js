function insertion(n) {
    for (let i = 0; i < n.length; i++){
        chave = n[i];
        j = i;
        while(j > 0 && chave < n[j - 1]){
            n[j] = n[j - 1];
            j -= 1;
        }
        n[j] = chave;
    }
    return n;
}