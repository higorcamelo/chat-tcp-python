import socket
import threading

# Lista para manter as conexões dos clientes
clientes = []

def aceitar_conexoes(ip, porta):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((ip, porta))
    servidor.listen(5)
    print(f"Servidor ouvindo em {ip}:{porta}")

    while True:
        cliente_socket, cliente_endereco = servidor.accept()
        print(f"Nova conexão de {cliente_endereco}")
        clientes.append(cliente_socket)

        # Iniciar uma nova thread para lidar com a conexão do cliente
        thread = threading.Thread(target=atender_cliente, args=(cliente_socket,))
        thread.start()

def atender_cliente(cliente_socket):
    while True:
        try:
            mensagem = cliente_socket.recv(1024)
            if not mensagem:
                break
            # Encaminhe a mensagem para todos os outros clientes conectados
            encaminhar_mensagem(cliente_socket, mensagem)
        except Exception as e:
            print(f"Erro na conexão do cliente: {e}")
            clientes.remove(cliente_socket)
            cliente_socket.close()
            break

def encaminhar_mensagem(emissor, mensagem):
    for cliente in clientes:
        if cliente != emissor:
            try:
                cliente.send(mensagem)
            except Exception as e:
                print(f"Erro ao encaminhar mensagem: {e}")
                clientes.remove(cliente)
                cliente.close()

if __name__ == '__main__':
    # Define o IP e a porta do servidor
    servidor_ip = '0.0.0.0'  # Pode ser 'localhost' para conexões locais
    servidor_porta = 12345  # Porta do servidor

    aceitar_conexoes(servidor_ip, servidor_porta)
