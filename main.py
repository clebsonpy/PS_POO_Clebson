from pessoa import Pessoa, Aluno, Professor, Administrador, Pesquisador

if __name__ == "__main__":

    aluno = Aluno("Clebson", "12345", "Graduação", "Clebsonpy", "clebson@algo.com")
    prof = Professor("Baldoino", "987654", "Baldoino", "baldoino@algo.com")
    admin = Administrador("Clara", "clarapy", "clara@algo.com")
    pesq = Pesquisador("Gabriel", "gabigol", "gabigol@algo.com")

    print(admin)
