import PySimpleGUI as sg


def jn_usuario():
    layout = [
        [sg.Text('Insira seu apelido:')],
        [sg.InputText(key = 'usuario')],
        [sg.Button('Ok')]
    ]
    return sg.Window('Chat TCP',Layout = layout, finalize = True)

def jn_chat():
    layout = [
        [sg.Text('Insira um IP para se conectar:')],
        [sg.InputText(key = 'ip')],
        [sg.Output(size = (30,60))],
        [sg.InputText(key = 'mensagem'), sg.Button(Enviar)]
    ]
    return sg.Window('Chat TCP', Layout = layout, finalize = True)


janela_usuario, janela_chat = jn_usuario(), None
while True:
    window, event, values = sg.read_all_windows()
    
    if window == janela_usuario and event == sg.WIN_CLOSED:
        break
    if window == janela_usuario and event == 'Ok':
        janela_chat = jn_chat()
        janela_usuario.hide()

