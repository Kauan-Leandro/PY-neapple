from PySimpleGUI import PySimpleGUI as sg

#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuario'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
#Janela
janela = sg.Window('Tela de login', layout)
#Ler os eventos
while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == 'Entrar':
        break
    if evento == 'Entrar':
        if valores['usuario'] == 'tk' and valores['senha'] == '123':
            print('Login realizado com sucesso!')
        else:
            print('Login ou senha inválidos!')
