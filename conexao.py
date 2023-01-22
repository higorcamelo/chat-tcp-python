import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('localhost',8888))

servidor.listen()

nome_usuario = ''
cliente, end = servidor.accept()
finalizado = False

while not finalizado:
    msg = cliente.recv(1024).decode('UTF-8')
    print(nome_usuario + ' ' + msg)

cliente.close()
servidor.close()