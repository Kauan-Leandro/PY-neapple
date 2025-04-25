from PySimpleGUI import PySimpleGUI as sg  # Importa o módulo PySimpleGUI para criar interfaces gráficas

# Define o tema da interface gráfica
sg.theme('DarkAmber')

# Função para validar os dados do registro
def validar_registro(values):
    # Verifica se o campo "nome" está vazio
    if not values['nome']:
        sg.popup('O campo Nome está vazio!')  # Exibe uma mensagem de erro
        return False
    # Verifica se o campo "email" está vazio
    elif not values['email']:
        sg.popup('O campo Email está vazio!')  # Exibe uma mensagem de erro
        return False
    # Verifica se o campo "senha" está vazio
    elif not values['senha']:
        sg.popup('O campo Senha está vazio!')  # Exibe uma mensagem de erro
        return False
    # Verifica se o email contém "@" e ".com" para validar o formato
    if '@' not in values['email'] or '.com' not in values['email']:
        sg.popup('Email inválido!')  # Exibe uma mensagem de erro
        return False
    return True  # Retorna True se todos os campos forem válidos

# Função para realizar o login
def realizar_login(values, dados_usuario):
    # Verifica se o email ou a senha não correspondem aos dados registrados
    if values['email_login'] != dados_usuario['email'] or values['senha_login'] != dados_usuario['senha']:
        sg.popup('Email ou senha incorretos!')  # Exibe uma mensagem de erro
        return False
    sg.popup('Login realizado com sucesso!')  # Exibe uma mensagem de sucesso
    return True  # Retorna True se o login for bem-sucedido

# Função para criar a janela de registro
def janela_registro():
    # Define o layout da janela de registro
    layout = [
        [sg.Text('Nome'), sg.Input(key='nome')],  # Campo para o nome
        [sg.Text('Email'), sg.Input(key='email')],  # Campo para o email
        [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],  # Campo para a senha (mascarada)
        [sg.Button('Confirmar')]  # Botão para confirmar o registro
    ]
    # Retorna a janela criada
    return sg.Window('Registro', layout=layout, finalize=True)

# Função para criar a janela de login
def janela_login():
    # Define o layout da janela de login
    layout = [
        [sg.Text('Olá,'), sg.Text(key='nome_exibido')],  # Exibe o nome do usuário registrado
        [sg.Text('Email')],  # Texto para o campo de email
        [sg.Input(key='email_login')],  # Campo para o email
        [sg.Text('Senha')],  # Texto para o campo de senha
        [sg.Input(key='senha_login', password_char='*')],  # Campo para a senha (mascarada)
        [sg.Button('Entrar')]  # Botão para realizar o login
    ]
    # Retorna a janela criada
    return sg.Window('Login', layout=layout, finalize=True)

# Cria as janelas iniciais: a de registro é exibida primeiro
janela1, janela2 = janela_registro(), None

# Dicionário para armazenar os dados do usuário registrado
dados_usuario = {}

# Loop principal para gerenciar os eventos das janelas
while True:
    # Lê os eventos e valores de todas as janelas abertas
    window, event, values = sg.read_all_windows()

    # Verifica se a janela de registro foi fechada
    if window == janela1 and event == sg.WIN_CLOSED:
        break  # Encerra o programa

    # Evento ao clicar no botão "Confirmar" na janela de registro
    if window == janela1 and event == 'Confirmar':
        # Valida os dados do registro
        if not validar_registro(values):
            continue  # Se os dados forem inválidos, volta para a janela de registro
        # Salva os dados do usuário no dicionário
        dados_usuario = {
            "nome": values['nome'],
            "email": values['email'],
            "senha": values['senha']
        }
        # Cria a janela de login e exibe o nome do usuário registrado
        janela2 = janela_login()
        janela2['nome_exibido'].update(values['nome'])
        janela1.hide()  # Oculta a janela de registro

    # Verifica se a janela de login foi fechada
    if window == janela2 and event == sg.WIN_CLOSED:
        janela2.close()  # Fecha a janela de login
        janela1.un_hide()  # Reexibe a janela de registro

    # Evento ao clicar no botão "Entrar" na janela de login
    if window == janela2 and event == 'Entrar':
        # Valida os dados de login
        if realizar_login(values, dados_usuario):
            sg.popup('Bem-vindo, {}!'.format(dados_usuario['nome']))  # Mensagem de boas-vindas
            janela2.close()  # Fecha a janela de login após o sucesso
            break  # Encerra o programa após login bem-sucedido
        else:
            # Mantém a janela de login aberta em caso de erro
            sg.popup('Tente novamente.')