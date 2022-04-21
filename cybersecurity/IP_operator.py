import ipaddress

ip = '192.168.0.1' #ip
ip2 = '192.168.0.0/24' #rede

endereco = ipaddress.ip_address(ip)
rede = ipaddress.ip_network(ip2, strict=False) #False=aceita entradas sendo errados e faz um ajuste

print(endereco)
print(endereco + 256)
print(endereco + 257)
print(rede)

for ip in rede: #imprime todos os ips da rede /24
    print(ip)