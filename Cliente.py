import re
import hashlib
class Cliente:
    """Classe responsavel pelos objetos do tipo Cliente """
    def __init__(self, usuario, senha):
        self.__usuario = usuario
        self.__senha = senha

    ##Getteres e setters
    @property
    def getUsuario(self):
        return self.__usuario
    @property
    def getSenha(self):
        return self.__senha

    def setUsuario(self,usuario):
        self.__usuario = usuario

    def setSenha(self, senha):
            self.__senha = senha

