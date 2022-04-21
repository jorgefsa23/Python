import os

print('-'*30)
#Criar variável que irá receber IP/Host a ser verificado:
ip_host = input("Digite o endereço IP ou HOST a ser verificado:")

print('-'*30)
os.system('ping -n 6 {}'.format(ip_host)) #definido 6 pings a ser enviados (se não definido, padrão é 4)
print('-'*30)