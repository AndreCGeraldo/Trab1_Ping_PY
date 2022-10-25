import subprocess
import os, platform
from subprocess import PIPE, Popen
from datetime import *
from time import sleep

url = []
ip = []
status = []
data = []
hora = []


def titulo(mensa, simbolo="=-"):
    print()
    print(mensa)
    print(simbolo*32)


def programa():
    titulo('')
    while True:
        data_e_hora_atuais = datetime.now()
        data_e_hora_em_texto = data_e_hora_atuais.strftime(f"%d/%m/%Y %H:%M:%S")

        def ping(host):
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            command = ['ping', param, '5', host]

            ping = Popen(
                command,
                stdout=PIPE,
                stderr=PIPE,
                shell=True
            )

            out, error = ping.communicate()

            return [subprocess.call(command), out.splitlines()]


        print("-"*26, "Bem Vindo", "-"*26)
        host = input("Digite uma URL: ")

        print("-"*26, "PINGANDO", "-"*27)

        [retornoPing, saidaPing] = ping(host)

        if (retornoPing == 0):
            print("------ HOST Ativo")
        else:
            print("------ OPS ---- Inativo")

        IPping = saidaPing[2].decode("utf-8")
        ips = IPping.split()[2][:-1]

        print("\n")
        print("-"*14, "URL | IP", "-"*14)
        print(f" {host:17s} | {ips}")
        print("\n")

        resp = ''
        while (len(resp) != 1) or (resp not in 'SN'):
            resp = input('Deseja Continuar? [S/N] ').upper()
            print("\n")

            url.append(host)
            ip.append(ips)
            if retornoPing == 0:
                status.append('Ativo')
            else:
                status.append('Inativo')
            data.append(data_e_hora_em_texto.split()[0])
            hora.append(data_e_hora_em_texto.split()[1])

        if resp == 'N':
            # print(f"URL", "-"*18, "|",  "IP", "-"*14, "|", "Status", "-"*7, "|", "data", "-"*7, "|", "Hora", "-"*7)

            # for i in range(len(url)):
            #     print(f"  {url[i]:20s} | {ip[i]:17s} | {status[i]:14s} | {data[i]:12s} | {hora[i]}")

            print("\n")
            print("#"*20, "FIM DE PROGRAMA", "#"*20)
            break


def salvar():
    with open("ping.txt", "w") as arq:
        for urls, ips, statuss, datas, horas in zip(url, ip, status, data, hora):
            arq.write(f"  {urls:20s} | {ips:17s} | {statuss:14s} | {datas:12s} | {horas}\n")
    
    print("\nSalvando Dados...")
    sleep(5)
    print("Dados Salvos com Sucesso!")


def lerTxt():
    with open("ping.txt", "r") as arq:
        ping = arq.read()
    print(f"\nURL", "-"*18, "|",  "IP", "-"*14, "|", "Status", "-"*7, "|", "data", "-"*7, "|", "Hora", "-"*7)
    print(ping)


def limpar():
    with open("ping.txt",'w') as arq:
        pass
    print("\nExcluíndo Dados...")
    sleep(5)
    print("Dados Excluídos com Sucesso!")


while True:
    titulo("Selecionar opção desejada: ", "=")
    print("1. Testar Ping")
    print("2. Salvar Testes de Ping")
    print("3. Exibir Dados")
    print("4. Excluir")
    print("5. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        programa()
    elif opcao == 2:
        salvar()
    elif opcao == 3:
        lerTxt()
    elif opcao == 4:
        limpar()
    else:
        break

