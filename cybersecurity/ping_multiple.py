import os
import time

with open('host.txt') as file:
    dump = file.read()
    dump = dump.splitlines()
    
    for ip in dump:
        print('Verficando o IP:', ip)
        print('-'*30)
        os.system('ping -n 2 {}'.format(ip)) #defino 2 pacotes de ping a ser enviado por ip/host
        print('-'*30)
        time.sleep(5)

