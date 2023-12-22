import re
from Cliente import Cliente
from CarregaCliente import CarregaCliente
import hashlib

class SalvaCliente:
    """Classe responsável por adicionar clientes ao Clientes.txt Separando usuario da senha por \t permite que
    o usuário tenha espaço no nome"""
    @staticmethod
    def salvar_clientes(nome_arquivo, cliente):
        with open(nome_arquivo, 'a') as arquivo:
            print(f"tentando salvar cliente {cliente.getUsuario}")
            if SalvaCliente.verificar_clientes(nome_arquivo, cliente) and SalvaCliente.validaSenha(cliente.getSenha):
                senha_hash = SalvaCliente.hash_senha(cliente.getSenha)
                arquivo.write(cliente.getUsuario+"\t"+senha_hash+"\n")
                print("Cliente adicionado com sucesso")
                return True
            else:
                print("Usuario já cadastrado")
                return False
            arquivo.close()

    @staticmethod
    def verificar_clientes(nome_arquivo, cliente):
        CarregaCliente.carregar_clientes(nome_arquivo)
        clientes = CarregaCliente.get_lista_clientes()
        usuarios_clientes = [c.getUsuario for c in clientes]
        if cliente.getUsuario not in usuarios_clientes:
            return True
        else:
            return False

    @staticmethod
    def validaSenha(senha):
        print("validando senha")
        regex = r"^(?=.*[!@#$%^&*()-_+=])(?=.*[A-Z])(?=.*\d)[A-Za-z\d!@#$%^&*()-_+=]{8,}$"
        if re.match(regex,senha):
            print(f'Senha valida')
            return True
        else:
            print("Senha invalida")
            return False
    @staticmethod
    # Funcoes para validar se a senha segue o regex e faz o hash antes de guardar
    def hash_senha(senha):
        return hashlib.sha256(senha.encode()).hexdigest()
