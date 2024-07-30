from studentapp.domain.Disciplina import Disciplina


class DisciplinaController:

    def __init__(self, repository):
        self.__repository = repository

    def get_all(self):
        return self.__repository.get_all()

    def adauga(self, id, nume, profesor):
        disciplina = Disciplina(id, nume, profesor)
        self.__repository.adauga(disciplina)

    def sterge(self, id):
        self.__repository.sterge(id)

    def modifica(self, id, nume_nou, profesor_nou):
        self.__repository.modifica(id, nume_nou, profesor_nou)