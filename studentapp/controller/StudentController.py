from studentapp.domain.Student import Student

class StudentController:

    def __init__(self, repository):
        self.__repository = repository

    def get_all(self):
        return self.__repository.get_all()

    def adauga(self, id_student, nume_student):
        student = Student(id_student, nume_student)
        self.__repository.adauga(student)