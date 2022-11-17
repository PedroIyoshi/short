nums = [3, 4, 15, 0, 1, 8, 41, 163, 84, 1384, 2, 0.5, 98];
 
function swap(n, i, a) {
    s = n[i];
    n[i] = n[i * 2 + a];
    n[i * 2 + a] = s
    return true;
}

function heap(n) {
    while(true){
        for (let i = 0; i < n.length - 1; i++) {
            if (i * 2 + 1 >= n.length) break;
            else if (i * 2 + 2 >= n.length) {
                f1 = n[i * 2 + 1]
                if (n[i] < f1) a = 1
                break;
            } else {
                f1 = n[i * 2 + 1];
                f2 = n[i * 2 + 2];
            }
            if (n[i] < f1 && n[i] < f2) {
                a = f1 > f2 ? 1 : 2;
            } else if (n[i] < f1) a = 1;
            else if (n[i] < f2) a = 2;
            trava = a == 0?false:swap(n, i, a);
        }
        if (!trava) break;
    }
}

console.log(heap(nums));