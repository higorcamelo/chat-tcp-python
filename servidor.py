import socket
import threading


host = ''

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((host, 8888))

servidor.listen()

apelido, clientes = []
cliente, end = servidor.accept()
finalizado = False

while not finalizado:
    msg = cliente.recv(1024).decode('UTF-8')
    print(apelido + ' ' + msg)

cliente.close()
servidor.close()