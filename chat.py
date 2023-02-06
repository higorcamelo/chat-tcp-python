import PySimpleGUI as sg
import servidor as sv

def jn_usuario():
    layout = [
        [sg.Text('Insira seu apelido:')],
        [sg.InputText(key = 'usuario')],
        [sg.Button('Ok')]
    ]
    return sg.Window('Chat TCP', layout, finalize = True)

def jn_chat(nome_usuario):
    layout = [
        [sg.Text('Olá, ' + nome_usuario)],
        [sg.Text('Insira um IP para se conectar:'), sg.Button('Conectar')],
        [sg.InputText(key = 'ip'), sg.Button('Hospedar conversa')],
        [sg.Multiline(size = (60,20), disabled = True)],
        [sg.InputText(key = 'mensagem'), sg.Button('Enviar')],
    ]
    return sg.Window('Chat TCP', layout, finalize = True)

def main():
    janela_usuario, janela_chat = jn_usuario(), None
    while True:
        window, event, values = sg.read_all_windows()
        
        if event == sg.WIN_CLOSED:
            break
        if window == janela_usuario and event == 'Ok':
            if(values['usuario'] == ''):
                sg.Popup('Insira um apelido válido')
            else:
                janela_chat = jn_chat(values['usuario'])
                janela_usuario.hide()
                if window == janela_chat and event == 'Enviar':
                    print('mensagem') #NAO PRINTA#         


if __name__ == '__main__':
    main()