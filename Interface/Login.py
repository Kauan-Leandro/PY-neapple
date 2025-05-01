from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout,
    QPushButton, QLineEdit, QCheckBox
)
from PySide6.QtCore import Qt
import sys

# Janela de cadastro
class Tela_de_Cadastro(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tela de Cadastro")
        self.setFixedSize(300, 200)

        # Criar layout
        layout = QVBoxLayout()

        # Criar widgets
        self.email = QLineEdit()
        self.email.setPlaceholderText("Insira seu Email")
        self.senha = QLineEdit()
        self.senha.setPlaceholderText("Insira sua Senha")
        self.senha.setEchoMode(QLineEdit.Password)
        self.senha_confirm = QLineEdit()
        self.senha_confirm.setPlaceholderText("Confirme sua Senha")
        self.senha_confirm.setEchoMode(QLineEdit.Password)
        self.aviso = QLabel()
        self.continuar = QPushButton("Continuar")
        self.mostrar_senhas_checkbox = QCheckBox("Mostrar Senhas")

        # Adicionar widgets ao layout
        layout.addWidget(self.email)
        layout.addWidget(self.senha)
        layout.addWidget(self.senha_confirm)
        layout.addWidget(self.mostrar_senhas_checkbox)
        layout.addWidget(self.aviso)
        layout.addWidget(self.continuar)

        # Configurar layout
        self.setLayout(layout)

        # Conectar botões e checkbox aos métodos
        self.continuar.clicked.connect(self.verificar_senhas)
        self.mostrar_senhas_checkbox.stateChanged.connect(self.mostrar_senhas)

        # Conectar o sinal returnPressed para mover o foco ou executar ações
        self.email.returnPressed.connect(lambda: self.senha.setFocus())
        self.senha.returnPressed.connect(lambda: self.senha_confirm.setFocus())
        self.senha_confirm.returnPressed.connect(self.verificar_senhas)

    def verificar_senhas(self):
        senha = self.senha.text()
        senha_confirm = self.senha_confirm.text()
        email = self.email.text()

        if senha != senha_confirm:
            self.aviso.setText("As senhas não coincidem!")
        elif email == "" or senha == "" or senha_confirm == "":
            self.aviso.setText("Preencha todos os campos!")
        elif '@' not in email or '.com' not in email:
            self.aviso.setText("Email inválido!")
        elif len(senha) < 6:
            self.aviso.setText("A senha deve ter pelo menos 6 caracteres!")
        else:
            self.aviso.setText("Cadastro realizado com sucesso!")
            # Passar valores para outra classe
            self.tela_login = Tela_de_Login(email, senha)
            self.tela_login.show()
            self.close()

    def mostrar_senhas(self):
        # Alternar entre mostrar e ocultar senhas com base no estado do checkbox
        if self.mostrar_senhas_checkbox.isChecked():
            self.senha.setEchoMode(QLineEdit.Normal)
            self.senha_confirm.setEchoMode(QLineEdit.Normal)
        else:
            self.senha.setEchoMode(QLineEdit.Password)
            self.senha_confirm.setEchoMode(QLineEdit.Password)


class Tela_de_Login(QWidget):
    def __init__(self, email, senha):
        super().__init__()
        self.setWindowTitle("Tela de Login")
        self.setFixedSize(300, 200)

        # Criar layout
        layout = QVBoxLayout()

        # Criar widgets
        self.email = QLineEdit()
        self.email.setPlaceholderText("Insira seu Email")
        self.senha = QLineEdit()
        self.senha.setEchoMode(QLineEdit.Password)
        self.senha.setPlaceholderText("Insira sua Senha")
        self.aviso = QLabel()
        self.confirmar = QPushButton("Confirmar")

        # Conectar o botão ao método verificar_login com lambda
        self.confirmar.clicked.connect(lambda: self.verificar_login(email, senha))

        # Adicionar widgets ao layout
        layout.addWidget(self.email)
        layout.addWidget(self.senha)
        layout.addWidget(self.aviso)
        layout.addWidget(self.confirmar)

        # Configurar layout
        self.setLayout(layout)

        # Conectar o sinal returnPressed para mover o foco ou executar ações
        self.email.returnPressed.connect(lambda: self.senha.setFocus())  # Foco na senha
        self.senha.returnPressed.connect(lambda: self.verificar_login(email, senha))  # Executar login

    def verificar_login(self, email, senha):
        # Aqui você pode adicionar a lógica de verificação de login
        if self.email.text() == "" or self.senha.text() == "":
            self.aviso.setText("Preencha todos os campos!")
        elif self.email.text() != email or self.senha.text() != senha:
            self.aviso.setText("Email ou senha incorretos!")
        else:
            self.tela_confirmacao = Tela_de_confirmação()
            self.tela_confirmacao.show()
            self.close()


class Tela_de_confirmação(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tela de Confirmação")

        # Criar layout
        layout = QVBoxLayout()

        # Criar widgets
        self.aviso = QLabel("Cadastro realizado com sucesso!")
        self.confirmar = QPushButton("Confirmar")
        self.confirmar.clicked.connect(self.close)

        # Adicionar widgets ao layout
        layout.addWidget(self.aviso)
        layout.addWidget(self.confirmar)

        # Configurar layout
        self.setLayout(layout)


# Código para rodar o aplicativo
if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = Tela_de_Cadastro()
    tela.show()
    sys.exit(app.exec())