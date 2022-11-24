function bubble(n) {
    while(true){
        pronto = true;
        for (let i = 1; i < n.length; i++) { 
            if (n[i - 1] > n[i]) {
                pronto = false;
                t = n[i];
                n[i] = n[i - 1];
                n[i - 1] = t;
            }
        }
        if (pronto) break;
    }
    return n;
}