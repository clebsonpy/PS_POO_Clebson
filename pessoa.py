class Pessoa():

    def __init__(self, nome, usuario, email):
        self.nome = nome
        self.usuario = usuario
        self.email = email

    def __str__(self):
        return ("Nome: "+ self.nome+"\nUsuário: "+ self.usuario+"\nE-mail: "
                +self.email)


class Aluno(Pessoa):

    def __init__(self, nome, matricula, grau, usuario, email):
        super().__init__(nome, usuario, email)
        self.matricula = matricula
        self.grau = grau

    def __str__(self):
        return ("Nome: "+ self.nome+"\nMatrícula: "+self.matricula
                +"\nUsuário: "+ self.usuario+"\nE-mail: "+self.email
                +"\nGrau: "+ self.grau)


class Professor(Pessoa):

    def __init__(self, nome, matricula, usuario, email):
        super().__init__(nome, usuario, email)
        self.matricula = matricula

class Administrador(Pessoa):

    def __init__(self, nome, usuario, email):
        super().__init__(nome, usuario, email)

class Pesquisador(Pessoa):

    def __init__(self, nome, usuario, email):
        super().__init__(nome, usuario, email)
