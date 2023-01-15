import PySimpleGUI as sg


def jn_usuario():
        layout = [
        [sg.Text('Insira seu apelido:')],
        [sg.InputText(key = 'usuario')],
        [sg.Button('Ok')]
        ]
        return sg.Window('Chat TCP',Layout = layout)

def jn_chat():
    layout = [
        [sg.Text('Olá,'+ jn_usuario(self))]
        [sg.Text('Insira um IP para se conectar:')],
        [sg.InputText(key = 'ip')],
        [sg.Output(size = (30,60))],
        [sg.InputText(key = 'mensagem'), sg.Button(Enviar)]
    ]
    return sg.Window('Chat TCP', Layout = layout)

def Iniciar(self):
    while True:
        self.evento, self.values = self.criarJanela.Read()
        if( self.evento == sg.WIN_CLOSED):
            break
        elif(self.evento == 'Ok'):
            nome_usuario = self.values['usuario']
            jn_chat()
            print(nome_usuario)

