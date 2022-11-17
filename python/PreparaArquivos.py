from itertools import islice
import os

# Separa o arquivo em arquivos menores, para que seja 
# possivel armazena-los na memoria
def preparaArquivos(n):
    quantidade = 1_000
    try:
        if not os.path.isdir("temp"):
            os.mkdir("temp")
        #verifica se a pasta temp existe
        
        for file in os.listdir("temp/"):
            os.remove("temp/" + file)
        #apaga todo o conteudo da pasta

        with open("../numeros/numeros_" + str(n) + ".txt") as arquivo:
            contador = 1
            posicao = 0
            while(True):
                intervalo = list(islice(arquivo, posicao, posicao + quantidade))
                if(intervalo == []): break
                temp = open("temp/n" + str(contador) + ".txt", 'w')
                intervalo[len(intervalo)-1] = intervalo[len(intervalo)-1].replace("\n", "")
                temp.write("".join(intervalo))
                temp.close()
                contador += 1
            arquivo.close()
        return True
    except Exception as e:
        print(e)
        return False