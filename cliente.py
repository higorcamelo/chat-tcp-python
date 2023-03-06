import socket
import threading

host = '127.0.0.1'
global apelido
global mensagem_temp

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    cliente.connect((host, 2525))
except ConnectionRefusedError:
    print('Não foi possível realizar a conrexão')

def receber():
    while True:
        try:
            msg = cliente.recv(1024)
            print(msg)
        except ConnectionResetError:
            print('A conexão foi desfeita inesperadamente...')
            cliente.close()
            break
        except Exception as e:
            print(str(e))
            print('Outro erro ocorreu')

def escrever():

    while True:
        msg = f'{apelido}: {input(mensagem_temp)}\n'
        cliente.send(msg.encode('UTF-8'))


def main():
    receber_thread = threading.Thread(target = receber)
    receber_thread.start()

    escrever_thread = threading.Thread(target = escrever)
    escrever_thread.start()

#main()