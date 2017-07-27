from typing import overload

class Cadastro():

    def __init__(self, nome, usuario, email):
        self.nome = nome
        self.usuario = usuario
        self.email = email

    @overload
    def cadastro(self):

    @cadastro.overload
    def cadastro(self, matricula):

    @cadastro.overload
    def cadastro(self, matricula, grau):

    def save(self):
        self.__class__.seq += 1
        self.id = self.__class__.seq
        self.__class__.objects.append(self)
