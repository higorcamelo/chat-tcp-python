import socket

cliente_socket = None

def conectar_servidor(ip, porta):
    global cliente_socket
    try:
        cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente_socket.connect((ip, porta))
        return True
    except Exception as e:
        print(f'Erro ao conectar: {e}')
        cliente_socket = None
        return False

def enviar_mensagem(mensagem):
    global cliente_socket
    if cliente_socket:
        cliente_socket.send(mensagem.encode())

def encerrar_conexao():
    global cliente_socket
    if cliente_socket:
        cliente_socket.close()
        cliente_socket = None
