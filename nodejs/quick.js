function quick(n) {
    if (n.length == 1) return n;
    if (n.length == 0) return [];
    let comparador = n[n.length - 1];   
    let maior = [], menor = [];

    n = n.slice(0, n.length - 1);
    if (n.length == 1) {
        if (n[0] <= comparador) return [n[0], comparador];
        return [comparador, n[0]];
    } 
    n.forEach(function (i) {
        if (i > comparador) maior.push(i);
        else menor.push(i);
    })
    menor = quick(menor);
    maior = quick(maior);

    menor.push(comparador);
    return menor.concat(maior);
} 