import socket
import threading

host = '127.0.0.1'

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((host, 8080))


servidor.listen()

apelidos, clientes = [], []


def transmissao(mensagem):
    for cliente in clientes:
        cliente.send(mensagem.encode('UTF-8'))


def handle(cliente):
    while True:
        try:
            msg = cliente.recv(1024).decode('UTF-8')
            print(f"{apelidos[clientes.index(cliente)]}: {msg}")
            transmissao(msg)
        except:
            index = clientes.index(cliente)
            clientes.remove(cliente)
            cliente.close()
            apelido = apelidos[index]
            print(f'{apelido} deixou a conversa...')
            apelidos.remove(apelido)
            break


def receber():
    while True:
        cliente, endereco = servidor.accept()
        print('Conectado com ' + str(endereco))

        cliente.send('APL'.encode('UTF-8'))
        apelido = cliente.recv(1024).decode('UTF-8') #######
        apelidos.append(apelido)
        clientes.append(cliente)

        print(f'{apelido} conectou-se ao servidor!')
        cliente.send('Conectado ao servidor!'.encode('UTF-8'))

        handle_thread = threading.Thread(target=handle, args = (cliente,))
        handle_thread.start()

def main():
    print('O servidor está aguardando...')
    receber()

main()
