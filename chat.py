import PySimpleGUI as sg
import cliente

def jn_usuario():
    layout = [
        [sg.Text('Insira seu apelido:')],
        [sg.InputText(key='-USUARIO-')],
        [sg.Button('Iniciar Chat')]
    ]
    return sg.Window('Chat TCP', layout, finalize=True)

def jn_chat(nome_usuario):
        
    layout = [
        [sg.Text(f'Olá, {nome_usuario}!', font=('Helvetica', 12))],
        [sg.Text('Insira o endereço IP do servidor e a porta para se conectar:')],
        [sg.InputText(key='-IP-', size=(15, 1), tooltip='Formato válido: 0.0.0.0'),
         sg.InputText(key='-PORTA-', size=(6, 1)),
         sg.Button('Conectar', key='-CONEX-'),
         sg.Button('Hospedar Conversa', key='-HOST-')],
        [sg.Multiline(key='-CONVERSATION-', size=(60, 15), disabled=True, autoscroll=True)],
        [sg.InputText(key='-MENSAGEM-', do_not_clear=False, size=(40, 1)), sg.Button('Enviar', key='-ENVIAR-')],
        [sg.Text('Status: Não conectado', key='-STATUS-', size=(30, 1), text_color='white')],
    ]
    return sg.Window('Chat TCP', layout, finalize=True)


def main():
    janela_usuario, janela_chat = jn_usuario(), None
    nome_usuario = ""

    while True:
        window, event, values = sg.read_all_windows()

        if event == sg.WIN_CLOSED:
            break

        if window == janela_usuario and event == 'Iniciar Chat':
            nome_usuario = values['-USUARIO-']
            if nome_usuario and len(nome_usuario) <= 50:
                janela_chat = jn_chat(nome_usuario)
                janela_usuario.hide()
            else:
                sg.Popup('Apelido inválido. Não pode ser nulo nem extremamente grande (limite: 50 caracteres).')

        if window == janela_chat:
            if event == '-ENVIAR-':
                mensagem = values['-MENSAGEM-']
                if mensagem:
                    # Adicione a mensagem ao histórico de conversa
                    conversation = window['-CONVERSATION-']
                    conversation.update(value=f'Você: {mensagem}\n', append=True)
                    # Lógica para enviar a mensagem
                    if cliente.conectado:
                        print(mensagem)
                    else:
                        sg.Popup('Nenhuma conexão foi estabelecida')
                else:
                    sg.Popup('Insira uma mensagem válida')
            elif event == '-CONEX-':
                # TODO: Lógica para conexão
                sg.popup('Conectar a', values['-IP-'], values['-PORTA-'])
                # Atualize o status de conexão
                window['-STATUS-'].update('Status: Conectando...', text_color='yellow')
            elif event == '-HOST-':
                # TODO: Lógica para hospedar a conversa
                sg.popup('Hospedando a conversa')
                # Atualize o status de conexão
                window['-STATUS-'].update('Status: Hospedando Conversa', text_color='green')
                if event == '-ENVIAR-':
                    mensagem = values['-MENSAGEM-']
                    if mensagem:
                        # Adicione a mensagem ao histórico de conversa
                        conversation = window['-CONVERSATION-']
                        conversation.update(value=f'Você: {mensagem}\n', append=True)
                        # TODO: Lógica para enviar a mensagem
                        if cliente.conectado:
                            print(mensagem)
                        else:
                            sg.Popup('Nenhuma conexão foi estabelecida')
                    else:
                        sg.Popup('Insira uma mensagem válida')
                elif event == '-CONEX-':
                    # TODO: Lógica para conexão
                    sg.popup('Conectar a', values['-IP-'], values['-PORTA-'])
                    # Atualize o status de conexão
                    window['-STATUS-'].update('Status: Conectando...', text_color='yellow')
                elif event == '-HOST-':
                    # TODO: Lógica para hospedar a conversa
                    sg.popup('Hospedando a conversa')
                    # Atualize o status de conexão
                    window['-STATUS-'].update('Status: Hospedando Conversa', text_color='green')


if __name__ == '__main__':
    main()
