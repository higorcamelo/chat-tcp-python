import socket
import threading

host = '127.0.0.1'

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect((host, 8080))

apelido = 'Teste'

def receber():
    while True:
        try:
            msg = cliente.recv(1024).decode('UTF-8')
            if msg == '!apl':
                cliente.send(apelido.encode('UTF-8'))
            else:
                print(msg)
        except:
            print('Um erro ocorrreu...')
            cliente.close()
            break

def escrever():
    while True:
        msg = f'{apelido}: {input("")}'

def main():
    receber_thread = threading.Thread(target=receber)
    receber_thread.start()

    escrever_thread = threading.Thread(target=escrever())
    escrever_thread.start()

main()