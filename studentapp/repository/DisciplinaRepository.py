class DisciplinaRepository:

    def __init__(self):
        self.__lista_discipline = []

    def get_all(self):
        return self.__lista_discipline

    def adauga(self, disciplina):
        if self.gaseste_disciplina_dupa_id(disciplina.get_id()) == None:
            self.__lista_discipline.append(disciplina)

    def sterge(self, id):
        if self.gaseste_disciplina_dupa_id(id) != None:
            disciplina = self.gaseste_disciplina_dupa_id(id)
            self.__lista_discipline.remove(disciplina)

    def modifica(self, id, nume_nou, profesor_nou):
        if self.gaseste_disciplina_dupa_id(id) != None:
            disciplina = self.gaseste_disciplina_dupa_id(id)
            disciplina.set_nume(nume_nou)
            disciplina.set_profesor(profesor_nou)

    def gaseste_disciplina_dupa_id(self, id):
        for i in range(0, len(self.__lista_discipline)):
            disciplina_curenta = self.__lista_discipline[i]
            if disciplina_curenta.get_id() == id:
                return disciplina_curenta
        return None