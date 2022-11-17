from Quick import quick
from insertion import insertion
from Bubble import bubble
import time

def stringToInt(s):
    s = s.split("\n")
    s = filter(None, s)#Retira todos os indices vazios
    s = list(map(lambda i:int(i), s))
    return s

for i in range(1, 8):
    with open("../numeros/numeros_" + str(i) + ".txt", "r") as file:
        numeros = stringToInt(file.read())
        startQuick = time.time()
        quick(numeros)
        endQuick = time.time()

        startBubble = time.time()
        bubble(numeros)
        endBubble = time.time()

        startInsertion = time.time()
        insertion(numeros)
        endInsertion = time.time()
    with open("resultado.txt", "a") as resultado:
        resultado.write("Quick sort numero:  " + str(i) + ": "+ str(endQuick-startQuick) + "\n")
        resultado.write("Bubble sort numero:  " + str(i) + ": "+ str(endBubble-startBubble) + "\n")
        resultado.write("Insertion sort numero:  " + str(i) + ": "+ str(endInsertion-startInsertion) + "\n")
