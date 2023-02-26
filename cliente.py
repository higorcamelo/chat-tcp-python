import socket
import threading

host = '127.0.0.1'

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    cliente.connect((host, 8080))
except ConnectionRefusedError:
    print('Não foi possível realizar a conrexão')

apelido = ''
#mensagem_temp = ''

def receber():
    while True:
        try:
            msg = cliente.recv(1024)
            print(msg)
        except:
            print('Um erro ocorrreu...')
            cliente.close()
            break

def escrever(mensagem_temp):
    while True:
        msg = f'{apelido}: {input(mensagem_temp)}'
        cliente.send(msg.encode('UTF-8'))

def main():
    receber_thread = threading.Thread(target = receber)
    receber_thread.start()

    escrever_thread = threading.Thread(target = escrever)
    escrever_thread.start()

main()