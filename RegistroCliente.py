import tkinter
from tkinter import *
from Cliente import Cliente
from CarregaCliente import CarregaCliente
from SalvaCliente import SalvaCliente
import MenuGUI

class RegistroCliente:
    """Interface para registro de novos usuários"""
    def __init__(self):
        self.master = tkinter.Tk()
        self.fontePadrao = ("Arial", "12")
        # Criando containers
        self.primeiroContainer = Frame(self.master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(self.master)
        self.segundoContainer["pady"] = 10
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(self.master)
        self.terceiroContainer["pady"] = 10
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(self.master)
        self.quartoContainer["pady"] = 10
        self.quartoContainer["padx"] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(self.master)
        self.quintoContainer["pady"] = 10
        self.quintoContainer["padx"] = 20
        self.quintoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Registro de Usuarios", font= self.fontePadrao)
        self.titulo["font"] = ("Arial", "12", "bold")
        self.titulo.pack()

        self.usuarioLabel = Label(self.segundoContainer, text="Usuario", font= self.fontePadrao)
        self.usuarioLabel.pack(side=LEFT)
        self.usuario = Entry(self.segundoContainer)
        self.usuario["width"] = 30
        self.usuario["font"] = self.fontePadrao
        self.usuario.pack(side=LEFT)

        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)
        self.senha = Entry(self.terceiroContainer, show="*")
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha.pack(side=LEFT)

        self.voltar = Button(self.quartoContainer)
        self.voltar["text"] = "Voltar"
        self.voltar["font"] = self.fontePadrao
        self.voltar["width"] = 12
        self.voltar["command"] = self.voltar_login
        self.voltar["pady"] = 10
        self.voltar.pack(side=LEFT)

        self.registrar = Button(self.quartoContainer)
        self.registrar["text"] = "Registrar"
        self.registrar["font"] = self.fontePadrao
        self.registrar["width"] = 12
        self.registrar["command"] = self.cadastrar_cliente
        self.registrar["pady"] = 10
        self.registrar.pack(side=LEFT)

        self.mensagem = Label(self.quintoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()
        self.master.mainloop()

    def voltar_login(self):
        self.master.destroy()
        MenuGUI.Application(tkinter.Tk())

    def cadastrar_cliente(self):
        usuario = self.usuario.get()
        senha = self.senha.get()
        cliente = Cliente(usuario,senha)
        if not SalvaCliente.verificar_clientes("Clientes.txt", cliente):
            self.mensagem["text"] = "Erro, usuario ja cadastrado"
        elif SalvaCliente.salvar_clientes("Clientes.txt",cliente):
            self.mensagem["text"] = "Cliente registrado com sucesso!"
        else:
            self.mensagem["text"] = "Erro, verifique se a senha \né segura o suficiente"

if __name__ == "__main__":
    RegistroCliente()