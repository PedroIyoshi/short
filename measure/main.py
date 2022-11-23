import psutil

pid = int(input("Insira o pid do processo: "))
cores = psutil.cpu_count()
try:
    p = psutil.Process(pid)
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
    arquivo.write(f'\n\n\n{p.name()} ==>    CPU: {maxCpu/cores},     RAM: {maxRam}')
