import socket

import sys


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 0 = TCP
except socket.error as e:
    print("A conexão falhou!!!")
    print("ERRO: {}".format(e))
    sys.exit()

print("Socket criado com sucesso")

HostAlvo = input("Digite o Host ou IP a ser conectado: ")
PortaAlvo = input("Digite a porta a ser conectada: ")

try:
    s.connect((HostAlvo, int(PortaAlvo)))
    print("Cliente TCP conectado com sucesso no Host:" + HostAlvo + "e na porta:" + PortaAlvo)
    s.shutdown(2)
except socket.error as e:
    print("A conexão falhou no Host:" + HostAlvo  + "na porta " + PortaAlvo)
    print("ERRO: {}".format(e))
    sys.exit()
