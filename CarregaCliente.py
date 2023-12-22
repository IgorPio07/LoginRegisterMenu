from Cliente import Cliente
class CarregaCliente:
    """Classe responsável por carregar os clientes já existentes no Clientes.txt e criar uma lista com eles"""
    clientes =[]
    @staticmethod
    def carregar_clientes(nome_arquivo):
        with open(nome_arquivo, "r") as arquivo:
            for linha in arquivo:
                linha = linha.strip()  # Remover espaços em branco e caracteres de nova linha
                usuario, senha_hash = linha.split("\t")
                CarregaCliente.clientes.append(Cliente(usuario, senha_hash))
            arquivo.close()

    @staticmethod
    def get_lista_clientes():
        return CarregaCliente.clientes