from itertools import islice
from PreparaArquivos import preparaArquivos 
from Bubble import bubble
from Quick import quick
from insertion import insertion
import os
import time
import cProfile

def listToString(n):
    s = list(map(lambda i:str(i)+"\n", n))
    return "".join(s)

def stringToInt(s):
    s = s.split("\n")
    s = filter(None, s)#Retira todos os indices vazios
    s = list(map(lambda i:int(i), s))
    return s


def arquivo(path, type, content = ""):
    if type == "r":
        with open(path, "r+") as arquivo:
            numeros = arquivo.read()
            numeros = stringToInt(numeros)
        return numeros
    elif type == "w":
        os.remove(path)
        with open(path, "w") as arquivo:
            arquivo.write(content)

def organiza(n, type):
    numeros = arquivo("temp/n" + str(n) + ".txt", "r")
    if(type == "bubble"):
        bubble(numeros)
    elif(type == "insertion"):
        insertion(numeros)
    else:
        quick(numeros)

def profileit(func):
    def wrapper(*args, **kwargs):
        datafn = func.__name__ + ".profile"  # Name the data file sensibly
        prof = cProfile.Profile()
        retval = prof.runcall(func, *args, **kwargs)
        prof.dump_stats(datafn)
        return retval

    return wrapper


@profileit
def main():
    os.remove("resultado.txt")
    open("resultado.txt", "w+").close()
    metodos = ["quick", "insertion"]
    for i in range(1, 5):
        if(preparaArquivos(i)):
            with open("resultado.txt", "a") as resultado:
                for type in metodos:
                    start = time.time()
                    for j in range(1, len(os.listdir("temp")) + 1):
                        organiza(j, type)
                    end = time.time()
                    resultado.write(type + " sort numero " + str(i) + ": " + str(end-start)[:5] + "\n")
                resultado.write("\n")
            print("fim")
        else:
            print("Erro")

main()