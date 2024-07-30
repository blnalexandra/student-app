from studentapp.controller.StudentController import StudentController
from studentapp.repository.StudentRepository import StudentRepository
from studentapp.controller.DisciplinaController import DisciplinaController
from studentapp.repository.DisciplinaRepository import DisciplinaRepository
from studentapp.ui.UI import UI


student_repository = StudentRepository()
disciplina_repository = DisciplinaRepository()

student_controller = StudentController(student_repository)
disciplina_controller = DisciplinaController(disciplina_repository)

ui = UI(student_controller, disciplina_controller)

ui.program()