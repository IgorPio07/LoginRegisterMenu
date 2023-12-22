from tkinter import * # Importando todos os componentes da biblioteca tkinter
from Cliente import Cliente
from CarregaCliente import CarregaCliente
from SalvaCliente import SalvaCliente
import RegistroCliente

class Application:
    """Classe responsavel pela interface gráfica principal de login"""
    clientes = CarregaCliente.get_lista_clientes() # Carrega a lista de clientes para fazer as verificacoes de loggin
    def __init__(self, master=None):
        # Labels da interface
        self.master = master
        self.fontePadrao = ("Arial", "12")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] =20
        self.quintoContainer.pack()
        # Valores e tipos de widgets
        self.titulo = Label(self.primeiroContainer, text="Dados do Usuário", font=self.fontePadrao)
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.usuarioLabel = Label(self.segundoContainer, text="Usuario", font= self.fontePadrao)
        self.usuarioLabel.pack(side=LEFT)
        self.usuario = Entry(self.segundoContainer)
        self.usuario["width"] = 30
        self.usuario["font"] = self.fontePadrao
        self.usuario.pack(side=LEFT)

        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)
        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha.pack(side=LEFT)

        self.login = Button(self.quartoContainer)
        self.login["text"] = "login"
        self.login["font"] = self.fontePadrao
        self.login["width"] = 12
        self.login["command"] = self.valida_usuario
        self.login.pack()

        self.registro = Button(self.quintoContainer)
        self.registro['text'] = "Register"
        self.registro["font"] = self.fontePadrao
        self.registro["width"] = 12
        self.registro["command"] = self.mostra_interface_registro
        self.registro.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    # Funcao que verifica se o usuario ja esta cadastrado e se a senha eh valida
    def valida_usuario(self):
        usuario = self.usuario.get()
        senha = self.senha.get()
        cliente = Cliente(usuario, SalvaCliente.hash_senha(senha))
        CarregaCliente.carregar_clientes("Clientes.txt")
        #Verificando se o clinete está no txt
        clientes = CarregaCliente.get_lista_clientes()
        for cli in clientes:
            if cli.getUsuario == cliente.getUsuario and cli.getSenha == cliente.getSenha:
                self.mensagem["text"] = "Login bem-sucedido"
                return
        self.mensagem["text"] = "Credenciais inválidas!"

    # Botao responsavel por fazer a interface de registro aparecer e destruir a atual
    def mostra_interface_registro(self):
        self.master.destroy()
        RegistroCliente.RegistroCliente()

# Instanciando a classe Tk() através da variável root
# Permite que os widgets(elementos da interface) apareçam e possam ser utilizados
def main():
    root = Tk()
    app = Application(root)
    root.mainloop()
# Main function
if __name__ == "__main__":
    main()


