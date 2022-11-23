import psutil

pid = input("Insira o pid do processo: ")

try:
    p = psutil.Process(int(pid)) 
except Exception as e:
    print("PID inválido\n" + e)

maxCpu = 0
maxRam = 0
 

try:
    while True:
        cpu = p.cpu_percent(interval=1.0)
        ram = p.memory_percent()

        if(cpu > maxCpu): maxCpu = cpu
        if(ram > maxRam): maxRam = ram
except Exception as e:
    print(e)

finally:
    arquivo = open("measure/resultado.txt", "a")
    arquivo.write(f'\n\n\n{p.name()} ==>    CPU: {maxCpu/4},     RAM: {maxRam}')
