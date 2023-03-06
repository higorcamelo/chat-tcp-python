import socket
import threading

host = '127.0.0.1'
global apelido
global mensagem_temp
conectado = False

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def conectar(apelido):
    global conectado
    global cliente
    try:
        cliente.connect((host, 2525))
        cliente.send(apelido.encode('UTF-8'))
        conectado = True
        return True
    except:
        print('Não foi possível realizar a conexão')
        return False

def receber():
    global conectado
    while conectado:
        try:
            msg = cliente.recv(1024)
            print(msg)
        except:
            print('A conexão foi desfeita inesperadamente...')
            cliente.close()
            conectado = False
            break

def escrever(mensagem):
    global conectado
    global cliente
    if conectado:
        msg = f'{apelido}: {mensagem}\n'
        cliente.send(msg.encode('UTF-8'))
    else:
        print('Nenhuma conexão foi estabelecida')

def main():
    receber_thread = threading.Thread(target = receber)
    receber_thread.start()