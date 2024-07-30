class StudentRepository:

    def __init__(self):
        self.__lista_studenti = []

    def get_all(self):
        return self.__lista_studenti

    def adauga(self, student):
        if self.gaseste_student_dupa_id(student.get_id()) == None:
            self.__lista_studenti.append(student)

    def gaseste_student_dupa_id(self, id):
        for i in range(0, len(self.__lista_studenti)):
            student_curent = self.__lista_studenti[i]
            if student_curent.get_id() == id:
                return student_curent
        return None