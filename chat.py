import PySimpleGUI as sg
import servidor

def jn_usuario():
    layout = [
        [sg.Text('Insira seu apelido:')],
        [sg.InputText(key = '-USUARIO-')],
        [sg.Button('Ok')]
    ]
    return sg.Window('Chat TCP', layout, finalize = True)

def jn_chat(nome_usuario):
    layout = [
        [sg.Text('Olá, ' + nome_usuario)],
        [sg.Text('Insira um IP para se conectar:'), sg.Button('Conectar', key = '-CONEX-')],
        [sg.InputText(key = '-IP-'), sg.Button('Hospedar conversa', key = '-HOST-')],
        [sg.Output(size = (60,20))],
        [sg.InputText(key = '-MENSAGEM-', do_not_clear=False), sg.Button('Enviar', key = '-ENVIAR-')],
    ]
    return sg.Window('Chat TCP', layout, finalize = True)

def jn_host(nome_usuario):
    layout = [
        [sg.Text('Este é o servidor do ' + nome_usuario)],
        [sg.Multiline(size = (60,20), disabled = True)],
        [sg.Button('Encerrar Conexão', key = '-FIM_CONEX-')],
    ]
    return sg.Window('Chat TCP', layout, finalize = True)

def main():
    janela_usuario, janela_chat, janela_host = jn_usuario(), None, None
    while True:
        window, event, values = sg.read_all_windows()
        
        if event == sg.WIN_CLOSED:
            break

        if window == janela_usuario and event == 'Ok':
            if(values['-USUARIO-'] == ''):
                sg.Popup('Insira um apelido válido')
            else:
                janela_chat = jn_chat(values['-USUARIO-'])
                janela_usuario.hide()

        if window == janela_chat and event == '-ENVIAR-':
            if (values['-MENSAGEM-'] == ''):
                pass
            else:
                print(values['-MENSAGEM-'])

        if window == janela_chat and event == '-CONEX-':
            pass

        if window == janela_chat and event == '-HOST-':
            servidor.main() # Crasha 


if __name__ == '__main__':
    main()