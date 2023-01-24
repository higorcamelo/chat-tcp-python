import socket
import threading

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('localhost', 8888))

apelido = ''

def receber():
    while True:
        try:
            msg = cliente.recv(1024).decode('UTF-8')
            if msg == 'APL':
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

receber_thread = threading.Thread(target=receber)
receber_thread.start()

escrever_thread = threading.Thread()