import socket
import threading

host = '127.0.0.1'

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((host, 8888))


servidor.listen()

apelidos, clientes = [], []
finalizado = False


def transmissao(mensagem):
    for client in clientes:
        client.send(mensagem)


def handle(client):
    while not finalizado:
        try:
            msg = cliente.recv(1024).decode('UTF-8')
            transmissao(msg)
        except:
            index = clientes.index(cliente)
            clientes.remove(client)
            client(close)
            apelido = apelidos[index]
            broadcast(apelido + ' deixou a conversa...'.encode('UTF-8'))
            apelidos.remove(apelido)
            finalizado = True



def receber():
    while True:
        cliente, endereco = servidor.accept()
        print('Conectado com ' + str(endereco))

        cliente.send('APL'.encode('UTF-8'))
        apelido = cliente.recv(1024).decode('UTF-8')
        apelidos.append(apelido)
        clientes.append(cliente)

        print('O apelido do cliente é ' + apelido)
        transmissao(apelido + ' entrou na conversa!'.encode('UTF-8'))
        cliente.send('Conectado ao servidor!'.encode('UTF-8'))

        thread = threading.Thread(target=handle, args= (cliente,))
        thread.start()

def main():
    print('O servidor está aguardando...')
    receber()