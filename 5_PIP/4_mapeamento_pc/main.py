import os
import platform
import psutil
import socket

# Retorna o resultado da versao do SO - no caso da maquina Ex: Sistema Operacional: Windows 11.
print(f"Sistema Operacional: {platform.system()} {platform.release()}.")

# Identifica o usuario da Maquina - Ex: Nome do usuario: ead.
print(f"Nome do usuario: {os.environ.get("USERNAME")}.")

# rastrea o IP-LOCAL - Ex: IPv4: 172.16.5.37.
print(f"IPv4: {socket.gethostbyname(socket.gethostname())}.")

# =============================================================
# Coleta informaçoes sobre as portas TCP e UDP
print("Portas abertas:\n")
connectall = psutil.net_connections(kind="inet")
# CRIA uma lista
only_udp = [conn for conn in psutil.net_connections(kind="inet") if conn.type == socket.SOCK_DGRAM]

# Separa as informaçoes sobre as portas
only_tcp_listening_ports = [conn.laddr.port for conn in connectall if conn.status == psutil.CONN_LISTEN] # TCP
only_udp_listening_ports = [conn.laddr.port for conn in only_udp] # UDP

# Remover as porta repetidas da lista
only_tcp_listening_ports = list(set(only_tcp_listening_ports))
only_udp_listening_ports = list(set(only_udp_listening_ports))

# Organizar as portas 
only_tcp_listening_ports.sort()
only_udp_listening_ports.sort()

# mostra as portas TCP
print("PORTAS TCP:\n")
for port in only_tcp_listening_ports:
    print(f"Portas TCP: {port} aberta.")

# mostra as portas UDP
print("PORTAS UDP:\n")
for port in only_udp_listening_ports:
    print(f"Portas UDP: {port} aberta.")




